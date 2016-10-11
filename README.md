# Hexagondola
Web interface for a raspberry-pi powered aerial tram with two continuous rotation servos (acting as motors), and two servos for a pan/tilt camera. Servo control is handled through a Pololu Maestro rather than the Pi's GPIO pins.

# Setup
Hexagondola requires:
* Pyserial (for maestro to work) 
* Flask

To run, simply run: `sudo python app.py`
