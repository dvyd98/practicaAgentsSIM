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
                print('%05.2f: Esquiador %s puja al telecadira. S`ha esperat %05.2f' % (env.now, name, env.now - start))
                start = env.now
                
                yield env.timeout(settings.time_telecadira)
                print('%05.2f: Esquiador %s ha arribat pel telecadira en %.1f' % (env.now, name,
                                                                                 env.now - start))
        else:
            with remuntador.request() as req:
                start = env.now
                yield req
                print('%05.2f: Esquiador %s puja al remuntador %s. S`ha esperat %05.2f' % (env.now, name, remuntador_name, env.now - start))
                start = env.now
                
                yield env.timeout(settings.time_remontador)
                print('%05.2f: Esquiador %s ha arribat pel remuntador %s en %.1f' % (env.now, name, remuntador_name,
                                                                                 env.now - start))
                
        pista = pista1
        pista_name = ""
        if not pista1.queue:
            pista = pista1
            pista_name = "1"
        elif not pista2.queue:
            pista = pista2
            pista_name = "2"
        elif not pista3.queue:
            pista = pista3
            pista_name = "3"
        elif not pista4.queue:
            pista = pista4
            pista_name = "4"
        else:
            min_length = 99999
            if (len(pista1.queue) <= min_length):
                min_length = len(pista1.queue)
                pista = pista1
                pista_name = "1"
            if (len(pista2.queue) <= min_length):
                min_length = len(pista2.queue)
                pista = pista2
                pista_name = "2"
            if (len(pista3.queue) <= min_length):
                min_length = len(pista3.queue)
                pista = pista3
                pista_name = "3"
            if (len(pista4.queue) <= min_length):
                min_length = len(pista4.queue)
                pista = pista4
                pista_name = "4"
        
        with pista.request() as req:
            start = env.now
            yield req
            print('%05.2f: Esquiador %s comença a baixar per la pista %s. S`ha esperat %05.2f' % (env.now, name, pista_name, env.now - start))
            start = env.now
            
            yield env.timeout(settings.fdistribution_pista())
            print('%05.2f: Esquiador %s acaba de baixar per la pista %s en %.1f' % (env.now, name, pista_name, env.now - start))
        
        settings.output += 1
                    
                    
        