from numpy import*
num = array(eval(input("digite o vetor de notas:")))
pesos = [2,1,5]

media_ponderada = dot(num, pesos)/sum(pesos)

print(round(media_ponderada,2))
