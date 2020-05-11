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
env = simpy.Environment()
telecadira = simpy.Resource(env, capacity=settings.capacitat_telecadira)    
remuntador1 = simpy.Resource(env, capacity=settings.capacitat_remuntador)
remuntador2 = simpy.Resource(env, capacity=settings.capacitat_remuntador)
pista1 = simpy.Resource(env, capacity=settings.capacitat_pista)
pista2 = simpy.Resource(env, capacity=settings.capacitat_pista)
pista3 = simpy.Resource(env, capacity=settings.capacitat_pista)
pista4 = simpy.Resource(env, capacity=settings.capacitat_pista)

#for i in range(4):
#    env.process(esquiador.esquiador(env, '%d' % i,telecadira,remuntador,pista))
#env.process(gsetup.grup_esquiador_setup(env, 'test', telecadira, remuntador, pista1, pista2, pista3, pista4))
env.process(sc.source(env, 0, telecadira, remuntador1, remuntador2, pista1, pista2, pista3, pista4))
env.run(until=settings.time_duration)

throughput = settings.output/settings.time_duration
remunt1_content = sum(settings.remunt1_cua) / len(settings.remunt1_cua)
remunt2_content = sum(settings.remunt2_cua) / len(settings.remunt2_cua)
telecadira_content = sum(settings.telecadira_cua) / len(settings.telecadira_cua)
pista1_content = sum(settings.pista1_cua) / len(settings.pista1_cua)
pista2_content = sum(settings.pista2_cua) / len(settings.pista2_cua)
pista3_content = sum(settings.pista3_cua) / len(settings.pista3_cua)
pista4_content = sum(settings.pista4_cua) / len(settings.pista4_cua)
print('Esquiadors generats: %d' % (settings.count))
print('Output: %05.2f' % (settings.output))
print('Throughput: %05.2f' % (throughput))
print('Mean content of remuntador1 queue: %05.2f' % (remunt1_content))
print('Mean content of remuntador2 queue: %05.2f' % (remunt2_content))
print('Mean content of telecadira queue: %05.2f' % (telecadira_content))
print('Mean content of pista1 queue: %05.2f' % (pista1_content))
print('Mean content of pista2 queue: %05.2f' % (pista2_content))
print('Mean content of pista3 queue: %05.2f' % (pista3_content))
print('Mean content of pista4 queue: %05.2f' % (pista4_content))

f = open("output.txt","w")
f.write('Esquiadors generats: %d \n' % (settings.count))
f.write('Output: %05.2f \n' % (settings.output))
f.write('Throughput: %05.2f \n' % (throughput))
f.write('Mean content of remuntador1 queue: %05.2f \n' % (remunt1_content))
f.write('Mean content of remuntador2 queue: %05.2f \n' % (remunt2_content))
f.write('Mean content of telecadira queue: %05.2f \n' % (telecadira_content))
f.write('Mean content of pista1 queue: %05.2f \n' % (pista1_content))
f.write('Mean content of pista2 queue: %05.2f \n' % (pista2_content))
f.write('Mean content of pista3 queue: %05.2f \n' % (pista3_content))
f.write('Mean content of pista4 queue: %05.2f \n' % (pista4_content))
f.close()