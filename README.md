# Introduction

umqtt_async is a simple to use, small mqtt client. It is designed to be fully asynchronous and used on constrained devices such as an ESP32.

To keep it simple and compatable with more usecases I have deisnged it so the network connectivity will be managed outside of umqtt_async and the status can be passed through if wanted.

## Features

1. QOS 1 supported with retansmission. Retransmission limit is changeable.
2. Automatic recovery from broker outage.
3. Non-blocking operation due to asynchronous design.

## Known Issues

The known issues are:
 1. Currently no SSL support.
 2. Automatic recovery from network outages still work in progress.

## Inspiration

I started by looking at:
 1. https://github.com/peterhinch/micropython-mqtt
 2. https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT
