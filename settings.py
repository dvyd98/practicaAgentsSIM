# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:27:34 2020

@author: Dvyd
"""

import numpy as np

def init():
    global count
    
    global output
    
    global remunt1_cua
    global remunt2_cua
    global telecadira_cua
    global pista1_cua
    global pista2_cua
    global pista3_cua
    global pista4_cua
    global ticks_count
    
    global time_remontador
    
    global time_telecadira
    
    global time_duration
    
    global distribution_pista
    global distribution_pista_mean
    
    global distribution_arribades
    global distribution_arribades_mean
    
    global distribution_num_esquiadors
    global distribution_num_esquiadors_mean
    
    global capacitat_remuntador
    global capacitat_telecadira
    global capacitat_pista
    
    count = 1
    output = 0
    
    remunt1_cua = []
    remunt2_cua = []
    telecadira_cua = []
    pista1_cua = []
    pista2_cua = []
    pista3_cua = []
    pista4_cua = []
    ticks_count = 0
    
    f = open("settings.txt", "r")
    f.readline()
    time_remontador = float(f.readline())
    f.readline()
    time_telecadira = float(f.readline())
    f.readline()
    time_duration = int(f.readline())
    
    f.readline()
    f.readline()
    
    distribution_pista = f.readline().strip()
    distribution_pista_mean = float(f.readline())
    f.readline()
    distribution_arribades = f.readline().strip()
    distribution_arribades_mean = float(f.readline())
    f.readline()
    distribution_num_esquiadors = f.readline().strip()
    distribution_num_esquiadors_mean = float(f.readline())
    
    f.readline()
    f.readline()
    
    capacitat_remuntador = int(f.readline())
    f.readline()
    capacitat_telecadira = int(f.readline())
    f.readline()
    capacitat_pista = int(f.readline())
    
def fdistribution_pista():
    if (distribution_pista in "normal"):
        return np.random.normal(loc=distribution_pista_mean)
    elif (distribution_pista in "exponential"):
        return np.random.exponential(scale=distribution_pista_mean)
    
def fdistribution_arribades():
    if (distribution_arribades in "normal"):
        return np.random.normal(loc=distribution_arribades_mean)
    elif (distribution_arribades in "exponential"):
        return np.random.exponential(scale=distribution_arribades_mean)
    
def fdistribution_num_esquiadors():
    if (distribution_num_esquiadors in "normal"):
        return np.random.normal(loc=distribution_num_esquiadors_mean)
    elif (distribution_num_esquiadors in "exponential"):
        return np.random.exponential(scale=distribution_num_esquiadors_mean)