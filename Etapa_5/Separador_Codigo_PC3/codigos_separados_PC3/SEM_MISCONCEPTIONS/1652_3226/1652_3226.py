from numpy import *
vet = input("").split(",")

resultado = zeros(5, dtype=int)
for i in vet:
    if(i=="B"):
        resultado[0]+=1
    if(i=="PA"):
        resultado[1]+=1
    if(i=="PR"):
        resultado[2]+=1
    if(i=="A"):
        resultado[3]+=1
    if(i=="I"):
        resultado[4]+=1

maior=max(resultado)
print(maior)
print(resultado)

