from numpy import*
notas = array(eval(input()))

i = 0
pesos = array([3,2,4,1,3])
m = notas * pesos
soma = sum(m)
media = soma / sum(pesos)

print(round(media, 2))