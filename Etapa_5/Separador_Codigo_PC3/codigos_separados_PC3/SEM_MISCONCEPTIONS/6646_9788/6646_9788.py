from numpy import * 

notas = array(eval(input('insira as notas: ')))
pesos = array([1,2,3])

num = notas * pesos

media = sum(num)/sum(pesos)

print(round(media,2))