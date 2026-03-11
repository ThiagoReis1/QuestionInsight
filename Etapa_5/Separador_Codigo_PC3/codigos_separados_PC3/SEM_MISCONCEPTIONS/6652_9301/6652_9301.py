from numpy import *
notas = array(eval(input("n: ")))
pesos = [2,2,6,1]
soma = sum(nota * peso for nota, peso in zip(notas,pesos))
soma_pesos = sum(pesos)
media = soma / soma_pesos
print(round(media,2))