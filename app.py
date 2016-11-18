#!/usr/bin/python
from flask import Flask, flash, redirect, render_template, request, session, abort
from time import sleep
from tram import Tram

TRAM = Tram()


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
    TRAM.pan_left()
 
@app.route("/pan-right")
def pan_right():
    TRAM.pan_right()

@app.route("/pan-up")
def pan_up():
    TRAM.pan_down()
  
@app.route("/pan-down")
def pan_down():
    TRAM.pan_up()
   
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
