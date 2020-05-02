# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:35:37 2020

@author: Dvyd
"""

import simpy
import itertools
import random
import numpy as np
import settings

class esquiador(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())
        
    def esquiador(env, name, telecadira, remuntador1, remuntador2, pista1, pista2, pista3, pista4):

        print('%05.2f: Esquiador %s arriba' % (env.now, name))
        remuntador = remuntador1
        remuntador_name = ""
        if not remuntador1.queue:
            remuntador = remuntador1
            remuntador_name = "1"
        elif not remuntador2.queue:
            remuntador = remuntador2
            remuntador_name = "2"
        else:
            if not telecadira.queue:
                remuntador_name = "0"
            elif (len(remuntador1.queue) <= len(remuntador2.queue)):
                remuntador = remuntador1
                remuntador_name = "1"
            else:
                remuntador = remuntador2
                remuntador_name = "2"
        
        if (remuntador_name == "0"): # telecadira buit
            with telecadira.request() as req:
                start = env.now
                yield req
                print('%05.2f: Esquiador %s puja al telecadira' % (env.now, name))
                
                yield env.timeout(1)
                print('%05.2f: Esquiador %s ha arribat pel telecadira en %.1f segons' % (env.now, name,
                                                                                 env.now - start))
        else:
            with remuntador.request() as req:
                start = env.now
                yield req
                print('%05.2f: Esquiador %s puja al remuntador %s' % (env.now, name, remuntador_name))
                
                yield env.timeout(1)
                print('%05.2f: Esquiador %s ha arribat pel remuntador %s en %.1f segons' % (env.now, name, remuntador_name,
                                                                                 env.now - start))
        with pista1.request() as req:
            start = env.now
            yield req
            print('%05.2f: Esquiador %s comença a baixar per la pista' % (env.now, name))
            
            yield env.timeout(0.5)
            print('%05.2f: Esquiador %s acaba de baixar per la pista en %.1f segons' % (env.now, name, env.now - start))
                    
                    
        