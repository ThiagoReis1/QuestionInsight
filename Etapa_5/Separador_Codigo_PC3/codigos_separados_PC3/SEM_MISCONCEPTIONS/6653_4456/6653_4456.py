import numpy as np

pesos = np.array([3,5,1])

notas = np.array(eval(input()))

multi = pesos * notas

soma_multi = sum(multi)
soma_pesos = sum(pesos)

media = soma_multi / soma_pesos

print(round(media,2))



