#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import call
import time
import sys
import webbrowser
from twitter import *

duration = input("Dauer für ein Pomodoro in min: ") #Dauer für ein Pomodoro/duration of one pomodoro
short_brk = input("Länge einer kurzen Pause in min: ") #Länge einer kurzen Pause/short break duration
long_brk = input("Länge einer langen Pause in min: ") #Länge einer langen Pause/long break duration
one_pomodori = input("Anzahl der auszuführenden Pomodori: ") #Anzahl der Pomodori/number of pomodori
duration_count = duration

def pomodoro(one_pomodori,short_brk,long_brk,duration,duration_count):
    for i in range(one_pomodori):
        duration = duration_count
        while duration > 0:
            print "%d min working..." % int(duration_count - duration)
            time.sleep(60)
            duration -= 1

        #start short break
        print "Take short %d min break" % short_brk
        webbrowser.open('http://vimeopro.com/ifamt/funktionelle-uebungen/video/83999082')
    	t = Twitter(
    	    auth=OAuth('???', '???', '???', '???'))

    	t.direct_messages.new(
        user="@???",
        text = ("BEWEGEN. SOFORT. UNBEDINGT."))

        time.sleep(60*int(short_brk))
        
        #stop short break
        
        print "Back to work..."

    	t = Twitter(
    	    auth=OAuth('???', '???', '???', '???'))

    	t.direct_messages.new(
        user="@???",
        text = ("WEITERMACHEN. Besser ist."))

    # start long break
    
    print "Well done.Take long %d min break" % long_brk

    t = Twitter(
    auth=OAuth('???', '???', '???', '???'))

    t.direct_messages.new(
    user="@???",
    text = ("BREAK! Lange Pause, sofort. LOS."))

    time.sleep(60*int(long_brk))
    
    #stop long break
    
    print "Back to work..."
    
    t = Twitter(
    	auth=OAuth('???','???','???','???'))
    t.direct_messages.new(
    user="@???",
    text=("Noch eine Runde?"))
    
#stop pomodori/start new pomodori
    
def wrapper():
    pomodoro(one_pomodori,short_brk,long_brk,duration,duration_count)
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

#-------------------------------------#
#Many thanks to aungthurhahein - I modified some of this Ideas: https://github.com/aungthurhahein/pomodoro_python
#-------------------------------------#