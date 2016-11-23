#!/usr/bin/python
from flask import Flask, flash, redirect, render_template, request, session, abort
from tram import Tram

TRAM = Tram()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('controller.html')
 
@app.route("/forward")
def forward():
    TRAM.move("forward")
 
@app.route("/backward")
def backward():
    TRAM.move("backward")

@app.route("/pan-left")
def pan_left():
    TRAM.pan_direction("left")
 
@app.route("/pan-right")
def pan_right():
    TRAM.pan_direction("right")

@app.route("/pan-up")
def pan_up():
    TRAM.tilt_direction("up")
  
@app.route("/pan-down")
def pan_down():
    TRAM.tilt_direction("down")
 
 
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=80)
    finally:
        TRAM.destroy()