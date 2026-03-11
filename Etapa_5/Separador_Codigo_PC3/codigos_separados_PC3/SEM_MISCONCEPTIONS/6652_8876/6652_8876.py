from numpy import *

notas = array(eval(input("Notas: ")), dtype=int)

pesos = array([2, 2, 6, 1])


multi1 = notas[0] * pesos[0]
multi2 = notas[1] * pesos[1]
multi3 = notas[2] * pesos[2]
multi4 = notas[3] * pesos[3]

media = (multi1 + multi2 + multi3 + multi4) / sum(pesos)

#Média
print(round(media, 2))