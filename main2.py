# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:39:45 2020

@author: Dvyd
"""

import simpy
import numpy as np
from esquiador import esquiador
from grup_esquiador_setup import grup_esquiador_setup as gsetup

env = simpy.Environment()
telecadira = simpy.Resource(env, capacity=4)    
remuntador = simpy.Resource(env, capacity=2)
pista = simpy.Resource(env, capacity=4)

#for i in range(4):
#    env.process(esquiador.esquiador(env, '%d' % i,telecadira,remuntador,pista))
env.process(gsetup.grup_esquiador_setup(env, 'test', telecadira, remuntador, pista))
env.run()