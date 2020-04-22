# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:38:27 2020

@author: Dvyd
"""

import simpy

class telecadira(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())
        
    def telecadira

