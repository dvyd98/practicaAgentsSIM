# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:12:32 2020

@author: Dvyd
"""
import simpy
import numpy as np
from car import Car

def driver(env, car):
    yield env.timeout(3)
    car.action.interrupt()

env = simpy.Environment()
bcs = simpy.Resource(env, capacity=2)
for i in range(4):
    env.process(Car.car(env, 'Car %d' % i, bcs, i*2, 5))
env.run()