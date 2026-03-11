from numpy import *
notas= array(eval(input("Digite o vetor notas: ")))

x= min(notas)
y= sum(notas) - x
z= size(notas) - 1
media= y/z
print(round(media, 2))
