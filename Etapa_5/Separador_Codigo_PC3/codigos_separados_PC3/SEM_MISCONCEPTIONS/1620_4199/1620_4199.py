from numpy import *
from math import *

tempo = array(eval(input(" tempo gasto nos banhos: "))) #vetor tempo
percentual = array(eval(input("percentual de abertura: "))) #vetor percentual
consumo1 = (tempo*percentual) #consumo primario
consumo2 = (consumo1/100) #consumo secundario
consumo3 = (consumo2*5) #consumo terciario
consumo_total_agua = sum(consumo3) #consumo total
print(round(consumo_total_agua,2))