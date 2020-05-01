# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:38:35 2020

@author: Dvyd
"""

import simpy
import itertools
import random
from esquiador_agrupat import esquiador_agrupat

class grup_esquiador_setup(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())
        
    def grup_esquiador_setup(env, num, telecadira, remuntador, pista):
        count = num
        #while (count < 5):
        num_esquiadors = random.randint(2,4)
        esqlist = []
        
        for i in range(num_esquiadors):
            esquiador = esquiador_agrupat(env)
            esq = esquiador.esquiador_agrupat(env, 'g%d-%d' % (count, i+1), telecadira, remuntador, pista)
            setattr(esquiador,'grup', count)
            env.process(esq)
            esqlist.append(esquiador)
            yield env.timeout(random.randint(1,3))
            
        for j in esqlist:
            setattr(j, 'potPujar', 1)
            
        for j in esqlist:
            while (getattr(j, 'isReady') == 0):
                yield env.timeout(0.1)
            
        for j in esqlist:
            setattr(j, 'potBaixar', 1)
