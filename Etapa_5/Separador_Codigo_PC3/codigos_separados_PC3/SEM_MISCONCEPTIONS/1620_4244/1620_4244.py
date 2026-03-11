from numpy import*
from math import *

tempo = array(eval(input("Tempo: ")))
percentual = array(eval(input("Percentual: ")))

consumo_A = (tempo*percentual)
consumo_B = consumo_A / 100
consumo_C = consumo_B * 5

consumo_total = sum(consumo_C)

print(round(consumo_total, 2))