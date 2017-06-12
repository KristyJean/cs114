"""This program will help me keep time when doing projects"""

import time


#Set up
print('Press enter to Start and Stop the program.. Press Ctrl-C to quit.')
input()                    # "Enter" IE the stop and go input
print('Start working!')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
timeTaken = 1

def pause(pauseFunction):
    if pauseFunction == p:
        time.sleep()
        print('Time Paused')
    elif pauseFunction == s:
         time.sleep(.1)
         print('Time Start')


try:
    while True:
            if input() == start:
                lapTime = round(time.time() - lastTime, 2)
                totalTime = round(time.time() - startTime, 2)
                print('Time Elasped for Task #%s: %s' % (timeTaken, totalTime), end='')
                timeTaken += 1
                lastTime = time.time() # reset the last lap time

except KeyboardInterrupt:

    print('It took you ' + str(hourAmount) + ' hours, ' + str(minuteAmount) + ' minutes, and ' + str(secondAmount) + ' seconds to complete this task.')
#The time calculations
hour = 3600
minute = 60
second = 1

timepassed = float(totalTime)

hourAmount = timepassed // hour
timepassed = timepassed - hourAmount * hour
minuteAmount = timepassed // minute
timepassed = timepassed - minuteAmount * minute
secondAmount = timepassed // second
timepassed = timepassed - secondAmount * second
