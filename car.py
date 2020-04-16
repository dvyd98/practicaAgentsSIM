# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:25:34 2020

@author: Dvyd
"""
import simpy

class Car(object):
     def __init__(self, env):
             self.env = env
             # Start the run process everytime an instance is created.
             self.action = env.process(self.run())
             
     def car(env, name, bcs, driving_time, charge_duration):
         # Simulate driving to the BCS
         yield env.timeout(driving_time)
         
         # Request one of its charging spots
         print('%s arriving at %d' % (name, env.now))
         with bcs.request() as req:
             yield req
             
             # Charge the battery
             print('%s starting to charge at %s' % (name, env.now))
             yield env.timeout(charge_duration)
             print('%s leaving the bcs at %s' % (name, env.now))
                 

     def run(self):
             while True:
                 print('Start parking and charging at %d' % self.env.now)
                 charge_duration = 5
                 # We may get interrupted while charging the battery
                 try:
                     yield self.env.process(self.charge(charge_duration))
                 except simpy.Interrupt:
                     # When we received an interrupt, we stop charging and
                     # switch to the "driving" state
                     print('Was interrupted. Hope, the battery is full enough ...')    
                     
                 # The charge process has finished and
                 # we can start driving again.
                 print('Start driving at %d' % self.env.now)
                 trip_duration = 2
                 yield self.env.timeout(trip_duration)

     def charge(self, duration):
             yield self.env.timeout(duration)