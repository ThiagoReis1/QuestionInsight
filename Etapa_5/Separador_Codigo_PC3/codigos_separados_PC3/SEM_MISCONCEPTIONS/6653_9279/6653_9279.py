from numpy import *
notas = array(eval(input("digite as notas: ")))
pesos = [3,5,1]
soma = sum(nota * peso for nota, peso in zip(notas,pesos))
soma_p = sum(pesos)
media = soma / soma_p
print(round(media,2))