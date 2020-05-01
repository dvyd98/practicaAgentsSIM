# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:35:37 2020

@author: Dvyd
"""

import simpy
import itertools
import random
import settings

class esquiador(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())
        
    def esquiador(env, name, telecadira, remuntador, pista):

        print('%05.2f: Esquiador %s arriba' % (env.now, name))
        
        with remuntador.request() as req:
            start = env.now
            yield req
            print('%05.2f: Esquiador %s puja al remuntador' % (env.now, name))
            
            yield env.timeout(0.1)
            print('%05.2f: Esquiador %s ha arribat pel remuntador en %.1f segons' % (env.now, name,
                                                                             env.now - start))
        with pista.request() as req:
            start = env.now
            yield req
            print('%05.2f: Esquiador %s comença a baixar per la pista' % (env.now, name))
            
            yield env.timeout(0.5)
            print('%05.2f: Esquiador %s acaba de baixar per la pista en %.1f segons' % (env.now, name, env.now - start))
                    
                    
        