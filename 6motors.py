#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random

# bottom hat is default address 0x60
bottomhat = Adafruit_MotorHAT(addr=0x60)
# top hat has A0 jumper closed, so its address 0x61
tophat = Adafruit_MotorHAT(addr=0x61)

# create empty threads (these will hold the stepper 1, 2 & 3 threads)
#stepperThreads = [threading.Thread(), threading.Thread(), threading.Thread()]

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    tophat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    tophat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    bottomhat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

#myStepper1 = bottomhat.getStepper(200, 1)      # 200 steps/rev, motor port #1
#myStepper2 = bottomhat.getStepper(200, 2)      # 200 steps/rev, motor port #2
#myStepper3 = tophat.getStepper(200, 1)      # 200 steps/rev, motor port #1

#myStepper1.setSpeed(60)          # 60 RPM
#myStepper2.setSpeed(30)          # 30 RPM
#myStepper3.setSpeed(15)          # 15 RPM

# get DC motors!
topMotor1 = tophat.getMotor(1)
topMotor2 = tophat.getMotor(2)
#topMotor3 = tophat.getMotor(3)
#topMotor4 = tophat.getMotor(4)

bottomMotor1 = bottomhat.getMotor(1)
bottomMotor2 = bottomhat.getMotor(2)
bottomMotor3 = bottomhat.getMotor(3)
bottomMotor4 = bottomhat.getMotor(4)

# set the speed to start, from 0 (off) to 255 (max speed)
topMotor1.setSpeed(50)
topMotor2.setSpeed(50)
#topMotor3.setSpeed(50)
#topMotor4.setSpeed(50)

bottomMotor1.setSpeed(50)
bottomMotor2.setSpeed(50)
bottomMotor3.setSpeed(50)
bottomMotor4.setSpeed(50)

# turn on motor
topMotor1.run(Adafruit_MotorHAT.FORWARD);
topMotor2.run(Adafruit_MotorHAT.FORWARD);
#topMotor3.run(Adafruit_MotorHAT.FORWARD);
#topMotor4.run(Adafruit_MotorHAT.FORWARD);

bottomMotor1.run(Adafruit_MotorHAT.FORWARD);
bottomMotor2.run(Adafruit_MotorHAT.FORWARD);
bottomMotor3.run(Adafruit_MotorHAT.FORWARD);
bottomMotor4.run(Adafruit_MotorHAT.FORWARD);


#stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE]
#steppers = [myStepper1, myStepper2, myStepper3]

#def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
 #   stepper.step(numsteps, direction, style)
    #print("Done")

while (True):
        print "Forwardtop1! "
        topMotor1.run(Adafruit_MotorHAT.FORWARD)
        print "Forwardtop2! "
        topMotor2.run(Adafruit_MotorHAT.FORWARD)
        print "Forwardbottom1! "
        bottomMotor1.run(Adafruit_MotorHAT.FORWARD)
        print "Forwardbottom2! "
        bottomMotor2.run(Adafruit_MotorHAT.FORWARD)
        print "Forwardbottom3! "
        bottomMotor3.run(Adafruit_MotorHAT.FORWARD)
        print "Forwardbottom4! "
        bottomMotor4.run(Adafruit_MotorHAT.FORWARD)

#       print "\tSpeed up..."
#       for i in range(255):
        topMotor1.setSpeed(50)
        topMotor2.setSpeed(50)
        bottomMotor1.setSpeed(50)
        bottomMotor2.setSpeed(50)
        bottomMotor3.setSpeed(50)
        bottomMotor4.setSpeed(50)
        time.sleep(10000.01)
