# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:39:45 2020

@author: Dvyd
"""

import simpy
import numpy as np
import settings
from esquiador import esquiador
from grup_esquiador_setup import grup_esquiador_setup as gsetup
from source import source as sc

settings.init()
env = simpy.rt.RealtimeEnvironment(factor=1.0)
telecadira = simpy.Resource(env, capacity=4)    
remuntador1 = simpy.Resource(env, capacity=2)
remuntador2 = simpy.Resource(env, capacity=2)
pista1 = simpy.Resource(env, capacity=2)
pista2 = simpy.Resource(env, capacity=2)
pista3 = simpy.Resource(env, capacity=2)
pista4 = simpy.Resource(env, capacity=2)

#for i in range(4):
#    env.process(esquiador.esquiador(env, '%d' % i,telecadira,remuntador,pista))
#env.process(gsetup.grup_esquiador_setup(env, 'test', telecadira, remuntador, pista1, pista2, pista3, pista4))
env.process(sc.source(env, 0, telecadira, remuntador1, remuntador2, pista1, pista2, pista3, pista4))
env.run(until=settings.time_duration)