from numpy import *

tempos = array(eval(input("")))
consumos = array(eval(input("")))

cons = 5

consumo = sum(tempos*(consumos/100)*cons)

print(round(consumo,2))