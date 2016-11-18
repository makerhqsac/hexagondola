#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

class Tram:

    def __init__(
            self, wheel1_pin=17, wheel2_pin=18,
            tilt_pin=13, pan_pin=15, frequency=100):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(wheel1_pin, GPIO.OUT)
        GPIO.setup(wheel2_pin, GPIO.OUT)
        GPIO.setup(tilt_pin, GPIO.OUT)
        GPIO.setup(pan_pin, GPIO.OUT)

        self.wheel1 = GPIO.PWM(wheel1_pin, frequency)
        self.wheel2 = GPIO.PWM(wheel2_pin, frequency)

        self.tilt = GPIO.PWM(tilt_pin, frequency)
        self.pan = GPIO.PWM(pan_pin, frequency)

    def start_wheels(self):
        """
        start_wheels: method for setting duty cycle to a value that will stop them from moving
        """
        self.wheel1.start(14)
        self.wheel2.start(14)

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
        full_forward_dc = 19
        slow_backward_dc = 11.5
        full_backward_dc = 8
        if direction == "forward":
            self.change_wheel_cycles(slow_forward_dc)
            sleep(1)
            self.change_wheel_cycles(full_forward_dc)
        else:
            self.change_wheel_cycles(slow_backward_dc)
            sleep(1)
            self.change_wheel_cycles(full_backward_dc)


    def soft_decelerate(self, direction):
        """
        soft_decelerate : when used, tram will slowly transition from max to zero speed.
        """
        slow_forward_dc = 17
        full_forward_dc = 19
        slow_backward_dc = 11.5
        full_backward_dc = 8
        if direction == "forward":
            self.change_wheel_cycles(full_forward_dc)
            sleep(1)
            self.change_wheel_cycles(slow_forward_dc)
        else:
            self.change_wheel_cycles(full_backward_dc)
            sleep(1)
            self.change_wheel_cycles(slow_backward_dc)


    def move(self, direction="forward", move_time=3):
        """
        move : moves either forward (default) or backward (any other direction passed in) for move_time seconds (default three seconds). Uses soft_acceleration and soft_deceleration for movement.
        """
        self.start_wheels()
        self.soft_accelerate(direction)
        sleep(1+move_time)
        self.soft_decelerate(direction)
        sleep(2)
        self.start_wheels

    def pan(self, direction):
        """
        pan : moves pan servo either to the left or to the right until it reaches either max left or max right.
        """

    def tilt(self, direction):
        """
        tilt: moves tilt servo either up or down until max value for either is reached.
        """
