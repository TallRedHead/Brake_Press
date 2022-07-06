from guizero import App, Text, Box
from datetime import datetime
#import RPi.GPIO as GPIO
import time

#resetbutton = Button(17)
#countbutton = Button(18)
#testing reboot pull


starttime = datetime.now()
textsize = 150
counterLimits = {'red':2,'yellow':3,'lightgreen':4}

count = 0
limit = 10

def addOne():
    global count
    count=count+1
    diff = count - limit
    counterN.value = count
    expectationN.value = limit
    differenceN.value = diff
    
    backgroundColor(counterN, count, counterLimits)
    backgroundColor(counter, count, counterLimits)
    time.delay(1)

def backgroundColor(text, value, counterLimits):
    for k,v in counterLimits.items():
        if value <= v: 
            text.bg = k
            break

'''
def checkInput(countbutton):
    global count
    uptimeN.value = int((datetime.now() - starttime).total_seconds())
    if GPIO.input(18):
        addOne()
        sleep(2)
    if GPIO.input(17):
        resetCounter()
        sleep(2)
'''

def resetCounter():
    global count, starttime
    starttime = datetime.now()
    count = 0
    counterN.value = count
    backgroundColor(counterN, count, counterLimits)
    backgroundColor(counter, count, counterLimits)
        
app = App(title = "Machine Status")
app.tk.attributes("-fullscreen",True)

counters = Box(app, align='top', width = 'fill')
counter = Text(counters, text="Counter", size = textsize, align='left', width = 'fill')
counterN = Text(counters, text=0, size = textsize, align='top')

expectations = Box(app, align='top', width = 'fill')
expectation = Text(expectations, text="Expectation", size = textsize, align='left', width = 'fill')
expectationN = Text(expectations, text=0, size = textsize, align='top')

differences = Box(app, align='top', width = 'fill')
difference = Text(differences, text="Difference", size = textsize, align='left', width = 'fill')
differenceN = Text(differences, text=0, size = textsize, align='top')

uptimes = Box(app, align='top', width = 'fill')
uptime = Text(uptimes, text="Uptime", size = textsize, align='left', width = 'fill')
uptimeN = Text(uptimes, text=0, size = textsize, align='top')

counter.repeat(100, addOne)

app.display()
