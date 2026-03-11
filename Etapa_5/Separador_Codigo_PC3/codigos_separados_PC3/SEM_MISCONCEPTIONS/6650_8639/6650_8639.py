from numpy import*
notas= array(eval(input()))
pesos=[4,3]
media= dot(notas,pesos)/ sum(pesos)
print(round(media,2))