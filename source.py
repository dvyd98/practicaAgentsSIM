# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:31:41 2020

@author: Dvyd
"""

import simpy
import itertools
import numpy as np
import random
import settings
from esquiador import esquiador
from esquiador_agrupat import esquiador_agrupat
from grup_esquiador_setup import grup_esquiador_setup as gsetup

class source(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())
        
    def source(env, num, telecadira, remuntador1, remuntador2, pista1, pista2, pista3, pista4):
        count_ind = 1
        count_grup = 1
        while(1):
            if (1 == 1):
                env.process(gsetup.grup_esquiador_setup(env, count_grup, telecadira, remuntador1, remuntador2, pista1, pista2, pista3, pista4))
                count_grup += 1
            else:
                env.process(esquiador.esquiador(env, '%d' % settings.count,telecadira, remuntador1, remuntador2, pista1, pista2, pista3, pista4))
                settings.count += 1
            print(settings.fdistribution_arribades())
            yield env.timeout(settings.fdistribution_arribades())
