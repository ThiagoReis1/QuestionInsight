from numpy import*

notas = eval(input("notas:"))

pesos = array([2, 2, 6, 1])

media= sum(notas*pesos)/sum(pesos)

print(round(media, 2))