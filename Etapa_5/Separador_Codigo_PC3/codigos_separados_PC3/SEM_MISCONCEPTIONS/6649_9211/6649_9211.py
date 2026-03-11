from numpy import*
notas = array(eval(input("v:")))
pesos = [3,2,4,1,3]
media = dot(notas , pesos) / sum(pesos)
print(round(media,2))