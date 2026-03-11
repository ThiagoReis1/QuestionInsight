from numpy import*
nota = eval(input("digite o vetor de notas: "))
pesos = array([4,3])
ponderada = sum(nota*pesos)/sum(pesos)

ponderada = round(ponderada, 2)
print(ponderada)