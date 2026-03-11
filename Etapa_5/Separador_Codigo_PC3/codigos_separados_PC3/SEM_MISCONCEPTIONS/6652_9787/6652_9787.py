from numpy import*

notas =array(eval(input()))
pesos = array([2, 2, 6, 1])

nm = notas * pesos

media = sum(nm)/sum(pesos)

print(round(media, 2))