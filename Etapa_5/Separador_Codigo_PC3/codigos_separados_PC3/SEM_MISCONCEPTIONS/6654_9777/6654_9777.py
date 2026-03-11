from numpy import*
notas = array(eval(input()))
pesos = [1, 3, 2, 5]

media = sum(notas * pesos) / sum(pesos)
print(round(media, 2))