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

        numEsquiadors = random.randint(1,4)
        print('Arriven %s esquiadors en l`instant %.1f' % (numEsquiadors, env.now))
        
        # Si ha arribat un grup d'esquiadors agafara el telecadira
        if (numEsquiadors > 1):
            while(telecadira.count > 0):
                print('Esperant que es buidi el telecadira')
            for i in range(numEsquiadors):
                with telecadira.request() as req:
                    start = env.now
                    yield req
                    print('Esquiador %s puja al telecadira' % (name))
                    
                    yield env.timeout(numEsquiadors)
                    print('Esquiador %s ha arribat pel telecadira en %.1f segons' % (name,
                                                                                     env.now - start))
                    
                    
        