


from numpy import *
a=array(eval(input("Digite o vetor:")))

x=0
cont=0
while(x<size(a)):
    if(a[x]<0):
        cont+=1
    x+=1

#print (cont)

vet=array(zeros(size(a)-cont,dtype=float))
    
j=0
k=0
while(j<size(a)):
    if(a[j]>=0):
        vet[k]=a[j]
        k+=1
    j+=1

print(vet)







 
