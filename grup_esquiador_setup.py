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
        
    def grup_esquiador_setup(env, name, telecadira, remuntador, pista):
        count = 0
        while (count < 20):
            count += 1
            num_esquiadors = random.randint(2,4)
            esqlist = []
            
            for i in range(num_esquiadors):
                esquiador = esquiador_agrupat(env)
                esq = esquiador.esquiador_agrupat(env, 'g%d %d' % (count, i+1), telecadira, remuntador, pista)
                setattr(esquiador,'grup', count)
                env.process(esq)
                esqlist.append(esquiador)
                
            for j in esqlist:
                while (getattr(j, 'isReady') == 0):
                    yield env.timeout(1)
                
            for j in esqlist:
                setattr(j, 'potBaixar', 1)
