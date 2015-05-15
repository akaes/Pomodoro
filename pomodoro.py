#-------------------------------------------------#
#!/usr/bin/env python
#-------------------------------------------------#

from subprocess import call
import time
import sys
from twitter import *

duration = 25 
short_brk = 5 
long_brk = 15 
One_pomodori = 5 
duration_count = duration

def pomodoro(One_pomodori,short_brk,long_brk,duration,duration_count):
    for i in range(1,One_pomodori):
        duration = duration_count
        while duration > 0:
            print "%d min working..." % int(duration_count - duration)
            time.sleep(60)
            duration -= 1

            print "Take short %d min break" % short_brk

    	t = Twitter(
    	    auth=OAuth('???', '???', '???', '???'))

    	t.direct_messages.new(
        user="@???",
        text = ("Kurze Pause. SOFORT. UNBEDINGT."))

        time.sleep(60*int(short_brk))
           print "Back to work..."

    	t = Twitter(
    	    auth=OAuth('???', '???', '???', '???'))

    	t.direct_messages.new(
        user="@???",
        text = ("WEITERMACHEN. Besser ist."))

        print "Well done.Take long %d min break" % long_brk

    t = Twitter(
    auth=OAuth('???', '???', '???', '???'))

    t.direct_messages.new(
    user="@???",
    text = ("BREAK! Lange Pause, sofort. LOS."))

    time.sleep(60*int(long_brk))

def wrapper():
    pomodoro(One_pomodori,short_brk,long_brk,duration,duration_count)
    call("play " +"chime/chime3.mp3", shell=True)
    print("A pomodori finished. Again?(y/n)")
    encore=raw_input(">")
    if encore == "y":
        wrapper()
    elif encore == "n":
        #tada
        exit(0)
    else:
        print "I dont't get that one.Try again"

if __name__ == "__main__":
    wrapper()
