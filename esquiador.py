# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:35:37 2020

@author: Dvyd
"""

import simpy
import itertools
import random

class esquiador(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())
        
    def esquiador(env, name, telecadira, remuntador, pista):

        print('Esquiador %s arriba en l`instant %.1f' % (name, env.now))
        
        with remuntador.request() as req:
            start = env.now
            yield req
            print('Esquiador %s puja al remuntador' % (name))
            
            yield env.timeout(1)
            print('Esquiador %s ha arribat pel remuntador en l`instant %.lf en %.1f segons' % (name, env.now,
                                                                             env.now - start))
                    
                    
        