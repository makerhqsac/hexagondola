#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

MIN_DC = 6
MAX_DC = 19

center_servo = 14
pan_value = 14
tilt_value = 14

class Tram:

    def __init__(
            self, wheel1_pin=18, wheel2_pin=17,
            tilt_pin=27, pan_pin=22, frequency=100):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(wheel1_pin, GPIO.OUT)
        GPIO.setup(wheel2_pin, GPIO.OUT)
        GPIO.setup(tilt_pin, GPIO.OUT)
        GPIO.setup(pan_pin, GPIO.OUT)

        self.wheel1 = GPIO.PWM(wheel1_pin, frequency)
        self.wheel2 = GPIO.PWM(wheel2_pin, frequency)

        self.start_wheels()

        self.tilt = GPIO.PWM(tilt_pin, frequency)
        self.pan = GPIO.PWM(pan_pin, frequency)

        self.start_pantilt()

    def start_pantilt(self):
        """
        start_wheels: method for setting duty cycle to a value that will stop them from moving
        """
        global center_servo
        self.tilt.start(center_servo)
        self.pan.start(center_servo)

    def start_wheels(self):
        """
        start_wheels: method for setting duty cycle to a value that will stop them from moving
        """
        global center_servo
        self.wheel1.start(center_servo)
        self.wheel2.start(center_servo)

    def change_wheel_cycles(self, dc):
        """
        change_wheel_cycles: method for changing duty cycle (i.e. speed) for both wheels at a time.
        """
        self.wheel1.ChangeDutyCycle(dc)
        self.wheel2.ChangeDutyCycle(dc)

    def soft_accelerate(self, direction):
        """
        soft_accelerate : when used, tram will slowly transition from zero to max speed.
        """
        slow_forward_dc = 17
        slow_backward_dc = 11

        if direction == "forward":
            for i in range(0,4):
                self.change_wheel_cycles(slow_forward_dc + i)
                sleep(0.25)
        else:
            for i in range(0,4):
                self.change_wheel_cycles(slow_backward_dc - i)
                sleep(0.25)


    def soft_decelerate(self, direction):
        """
        soft_decelerate : when used, tram will slowly transition from max to zero speed.
        """
        full_forward_dc = 21
        full_backward_dc = 7
        if direction == "forward":
            for i in range(0,4):
                self.change_wheel_cycles(full_forward_dc - i)
                sleep(0.25)
        else:
            for i in range(0,4):
                self.change_wheel_cycles(full_backward_dc + i)
                sleep(0.25)


    def move(self, direction="forward", move_time=3):
        """
        move : moves either forward (default) or backward (any other direction passed in) for move_time seconds (default three seconds). Uses soft_acceleration and soft_deceleration for movement.
        """
        self.start_wheels()
        self.soft_accelerate(direction)
        sleep(1+move_time)
        self.soft_decelerate(direction)
        sleep(2)
        self.change_wheel_cycles(14)
        return "Tram moved %s" % direction

    def add_angle(self,motor):
        global pan_value, tilt_value
        if motor == "tilt":
            tilt_value = tilt_value + 1
            if tilt_value > MAX_DC:
                tilt_value = MAX_DC
            self.tilt.ChangeDutyCycle(tilt_value)
        else:
            pan_value = pan_value + 1
            if pan_value > MAX_DC:
                pan_value = MAX_DC
            self.pan.ChangeDutyCycle(pan_value)


    def sub_angle(self,motor):
        global pan_value, tilt_value
        if motor == "tilt":
            tilt_value = tilt_value - 1
            if tilt_value < MIN_DC:
                tilt_value = MIN_DC
            self.tilt.ChangeDutyCycle(tilt_value)
        else:
            pan_value = pan_value - 1
            if pan_value < MIN_DC:
                pan_value = MIN_DC
            self.pan.ChangeDutyCycle(pan_value)

    def pan_direction(self, direction):
        """
        pan : moves pan servo either to the left or to the right until it reaches either max left or max right.
        """
        global pan_value
        if direction == "left":
            self.add_angle("pan")
        else:
            self.sub_angle("pan")
        return "Pan Value is now %d" % pan_value

    def tilt_direction(self, direction):
        """
        tilt: moves tilt servo either up or down until max value for either is reached.
        """
        global tilt_value
        if direction == "up":
            self.add_angle("tilt")
        else:
            self.sub_angle("tilt")
        return "Tilt Value is now %d" % tilt_value

    def destroy(self):
        GPIO.cleanup()