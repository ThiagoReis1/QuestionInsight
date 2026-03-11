from numpy import*

notas=array(eval(input()))

pesos=array([3,2,4,1,3])

num=notas*pesos

media= sum(num)/sum(pesos)

print(round(media, 2))
