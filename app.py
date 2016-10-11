from flask import Flask, flash, redirect, render_template, request, session, abort
from time import sleep
import maestro

# Servo motor 0 stops at 1633 
# Servo motor 1 stops at 1621
SERVO0_HOME = 6532
SERVO1_HOME = 6484

PAN_HOME = 6000
PAN_MAX = 8000
PAN_MIN = 4000

# Set target for moving forward
SERVO0_FORWARD = 7000
SERVO1_FORWARD = 6952

# Set target for moving backwards
SERVO0_BACKWARD = 6064
SERVO1_BACKWARD = 6016

#servo = maestro.Controller()
app = Flask(__name__)

pan_vertical = 6000
pan_horizontal = 6000

def pan_change(direction):
    global pan_vertical
    global pan_horizontal
    if direction == "left":
        pan_horizontal -= 250
    if direction == "right":
        pan_horizontal += 250
    if direction == "down":
        pan_vertical += 250
    if direction == "up":
        pan_vertical -= 250
    if pan_vertical < PAN_MIN:
        pan_vertical = PAN_MIN
    if pan_vertical > PAN_MAX:
        pan_vertical = PAN_MAX
    if pan_horizontal > PAN_MAX:
        pan_horizontal = PAN_MAX
    if pan_horizontal < PAN_MIN:
        pan_horizontal = PAN_MIN
    servo.setTarget(2,pan_horizontal)  
    servo.setTarget(3,pan_vertical)




def move_forward():
    servo.setTarget(0,SERVO0_HOME)  
    servo.setTarget(1,SERVO1_HOME)
    servo.setAccel(1,4)
    servo.setAccel(0,4)
    servo.setTarget(0,SERVO0_FORWARD) 
    servo.setTarget(1,6952) 
    sleep(1)
    servo.setTarget(0,SERVO0_HOME)  
    servo.setTarget(1,SERVO1_HOME)

def move_backward():
    servo.setTarget(0,SERVO0_HOME)  
    servo.setTarget(1,SERVO1_HOME)
    servo.setAccel(1,4)
    servo.setAccel(0,4)
    servo.setTarget(0,6064) 
    servo.setTarget(1,6016) 
    sleep(1)
    servo.setTarget(0,SERVO0_HOME)  
    servo.setTarget(1,SERVO1_HOME)


@app.route("/")
def index():
    return render_template('controller.html')
 
@app.route("/forward")
def forward():
    move_forward()
 
@app.route("/backward")
def backward():
    move_backward()

@app.route("/pan-left")
def pan_left():
    pan_change("left")
 
@app.route("/pan-right")
def pan_right():
    pan_change("right")

@app.route("/pan-up")
def pan_up():
    pan_change("up")
  
@app.route("/pan-down")
def pan_down():
    pan_change("down")
   
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
