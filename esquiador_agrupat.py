# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:50:46 2020

@author: Dvyd
"""

import simpy
import itertools
import random

class esquiador_agrupat(object):
    
    def __init__(self, env):
        self.grup = 0
        self.isReady = 0
        self.potBaixar = 0
        self.env = env
        
    def esquiador_agrupat(self, env, name, telecadira, remuntador, pista):

        print('%.lf: Esquiador %s arriba' % (env.now, name))
        

        with remuntador.request() as req:
            start = env.now
            yield req
            print('%.lf: Esquiador %s puja al remuntador' % (env.now, name))
            
            yield env.timeout(1)
            print('%.lf: Esquiador %s ha arribat pel remuntador en %.1f segons' % (env.now, name,
                                                                             env.now - start))
        self.isReady = 1
        print('%.lf: Esquiador %s esta apunt per baixar' % (env.now, name))
        while (self.potBaixar != 1):
            print('%.lf: Esquiador %s encara no pot baixar' % (env.now, name))
            yield env.timeout(1)
                    
                    
        