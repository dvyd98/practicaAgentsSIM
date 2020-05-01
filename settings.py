# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:27:34 2020

@author: Dvyd
"""

def init():
    global output
    
    global time_remontador
    
    global time_telecadira
    
    global time_pista
    
    global time_duration
    
    output = 0
    
    f = open("settings.txt", "r")
    time_remontador = float(f.readline())
    time_telecadira = float(f.readline())
    time_pista = float(f.readline())
    time_duration = int(f.readline())