from numpy import *
vetor_notas = array(eval(input("Insira o vetor de notas: ")))

notas = sum(vetor_notas)
notas = notas- min(vetor_notas)
media = notas /(size(vetor_notas) - 1)
print(round(media, 2))