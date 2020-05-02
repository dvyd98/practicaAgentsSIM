# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:50:46 2020

@author: Dvyd
"""

import simpy
import itertools
import numpy as np
import random
import settings

class esquiador_agrupat(object):
    
    def __init__(self, env):
        self.grup = 0
        self.isReady = 0
        self.potBaixar = 0
        self.potPujar = 0
        self.env = env
        
    def esquiador_agrupat(self, env, name, telecadira, remuntador1, remuntador2, pista1, pista2, pista3, pista4):

        print('%05.2f: Esquiador %s arriba' % (env.now, name))
        
        while (self.potPujar != 1):
             #print('%f: Esquiador %s espera als seus companys per pujar' % (env.now, name))
            yield env.timeout(0.1)
        

        with remuntador1.request() as req:
            start = env.now
            yield req
            print('%05.2f: Esquiador %s puja al remuntador' % (env.now, name))
            
            yield env.timeout(0.1)
            print('%05.2f: Esquiador %s ha arribat pel remuntador en %.1f segons' % (env.now, name,
                                                                             env.now - start))
            
        self.isReady = 1
        print('%05.2f: Esquiador %s esta apunt per baixar' % (env.now, name))
        
        while (self.potBaixar != 1):
            #print('%f: Esquiador %s espera als seus companys per baixar' % (env.now, name))
            yield env.timeout(0.1)
            
        with pista1.request() as req:
            start = env.now
            yield req
            print('%05.2f: Esquiador %s comença a baixar per la pista' % (env.now, name))
            
            yield env.timeout(0.5)
            print('%05.2f: Esquiador %s acaba de baixar per la pista en %.1f segons' % (env.now, name, env.now - start))
                    
                    
        