# Hexagondola
## Overview
Web interface for a raspberry-pi powered aerial tram with two continuous rotation servos (acting as motors), and two servos for a pan/tilt camera.

To run, simply run: `sudo python app.py`

## Interfacing with Webcam

We currently employ an iframe of [mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer) on port 8080. Follow the relevant setup instructions on the pi in order to enable the camera.