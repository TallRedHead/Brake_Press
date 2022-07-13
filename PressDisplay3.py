
from guizero import App, Text, Box, TextBox
from datetime import datetime
import RPi.GPIO as GPIO
import time

# Settings. Change these values to get desired results

countPin = 13 #IO27 on terminal block
GPIO.setmode(GPIO.BOARD)
GPIO.setup(countPin, GPIO.IN)

starttime = datetime.now()
shiftstart = starttime.replace (hour=8, minute=0)
minutesPerDay = 8*60
textsize = 175
differenceLimits = {'red':60, 'orange':75, 'yellow':90, 'lightgreen':200}
count = 0
shiftgoal = 1000
timeElapsedLimit = 6
LoopTime_ms = 100
lastPulse = datetime.now()
minPulse = 1 
maxPulse = 5



def addOne(countPin=countPin):
    global count, lastPulse, percentage
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(countPin, GPIO.IN)
    if datetime.now().hour == 3: count = 0
    timePercentage = ((datetime.now().hour - 8) * 60 + datetime.now().minute)/minutesPerDay    
    if timePercentage < 0: timePercentage = 0
    elif timePercentage > 1: timePercentage = 1
    goal = int(timePercentage * int (shiftGoalN.value))
    try:
        percentage = abs(int(count/goal*100))
    except ZeroDivisionError:
        percentage = 0

    timeElapsed = (datetime.now()-lastPulse).seconds > timeElapsedLimit
    diff = count - goal
    differenceN.value = str(percentage)+'%'
    backgroundColor(differenceN, percentage, differenceLimits)
    expectationN.value = goal
    
    try:
        if not GPIO.input(countPin) and timeElapsed==True and (datetime.now()-lastPulse).seconds > minPulse and (datetime.now()-lastPulse).seconds < maxPulse:
            count=count+1
            
            counterN.value = count
            lastPulse = datetime.now()
    finally:
        GPIO.cleanup()
    
def backgroundColor(text, value, counterLimits):
    for k,v in counterLimits.items():
        if value <= v: 
            app.bg = k
            break

# Application Layout with a Box describing each row, with the text and value insize each box

app = App(title = "Machine Status")
app.tk.attributes("-fullscreen",True)

counters = Box(app, align='top', width = 'fill')
counter = Text(counters, text="Bend Count     ", size = textsize, align='left', width = 'fill')
counterN = Text(counters, text=0, size = textsize, align='top')

expectations = Box(app, align='top', width = 'fill')
expectation = Text(expectations, text="Goal             ", size = textsize, align='left', width = 'fill')
expectationN = Text(expectations, text=0, size = textsize, align='top')

ShiftGoals = Box(app, align='top', width = 'fill')
shiftGoal = Text(ShiftGoals, text="Shift Goal   ", size = textsize, align='left', width = 'fill')
shiftGoalN = TextBox(ShiftGoals, text="100", width = 200, align='top')
shiftGoalN.text_size = textsize

differences = Box(app, align='top', width = 'fill')
difference = Text(differences, text="Efficiency   ", size = textsize, align='left', width = 'fill')
differenceN = Text(differences, text=0, size = textsize, align='right')

counter.repeat(LoopTime_ms, addOne)

app.display()
