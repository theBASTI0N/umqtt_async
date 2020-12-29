from umqtt_async import MQTTClient
try:
    import uasyncio as asyncio
    import time
    import machine
    import network
except:
    import asyncio
import json
import sys


# Variables
BROKER = "test.mosquitto.org"
PORT = 1883

# ESP32 Variables
SSID = "Your SSID"
WIFI_PASS = "Your Password"

if sys.platform == "esp32":
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, WIFI_PASS)
    time.sleep(5)

client = MQTTClient(broker=BROKER, port=PORT, keep_alive=20)

async def main():
    await client.connect()
    await asyncio.sleep(1)
    
    counter = 0
    while counter <= 10: 
        if client.is_connected:
            msg = json.dumps({"test" : counter})
            await client.publish(client.client_id + "/TestTopic", msg)
            await asyncio.sleep(0.050)
            counter+=1
        else:
            await asyncio.sleep(0.5)
    await client.unsubscribe(client.client_id + "/TestTopic")
    await client.subscribe(client.client_id + "/TestTopic2")
    
    counter = 0
    while counter <= 20: 
        if client.is_connected:
            msg = json.dumps({"test" : counter})
            await client.publish(client.client_id + "/TestTopic2", msg, qos=1)
            await asyncio.sleep(0.050)
            counter+=1
        else:
            await asyncio.sleep(0.5)
    
    await client.unsubscribe(client.client_id + "/TestTopic2")
    
    await client.disconnect()

def callback(topic, msg): 
    print(topic, msg)

async def on_connection(): 
    await client.subscribe(client.client_id + "/TestTopic", 0)

async def end():
    await client.disconnect()

loop = asyncio.get_event_loop()

client.network_status = True
# Not yet supported
# client.set_ssl(ssl=True)
client.on_message_cb = callback
client.on_connection_cb = on_connection
loop.run_until_complete(main())

print("umqtt_async test complete.")