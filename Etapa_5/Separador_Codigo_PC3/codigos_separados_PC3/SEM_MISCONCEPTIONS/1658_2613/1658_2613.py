
from numpy import *
vet = input("").split(",")

resultado = zeros(5, dtype=int)
for i in vet:
    if(i=="CHN"):
        resultado[0]+=1
    if(i=="JPN"):
        resultado[1]+=1
    if(i=="KOR"):
        resultado[2]+=1
    if(i=="MGL"):
        resultado[3]+=1
    if(i=="THA"):
        resultado[4]+=1

maior=max(resultado)
print(maior)
print(resultado)
