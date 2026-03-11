from numpy import *
vet = array(eval(input()))

contador=0
resultado=[]
for i in range(size(vet)):
    if(vet[i]>=70):
        contador=contador+1
        resultado.append(i)

print(contador)
resultado=array(resultado)
print(resultado)