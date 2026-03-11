from numpy import *
string = input().split(',')

vet = zeros(5,dtype=int)

for i in range(len(string)):
    if(string[i]=="AC"):
        vet[0]=vet[0]+1
    if(string[i]=="AM"):
        vet[1]=vet[1]+1
    if(string[i]=="PA"):
        vet[2]=vet[2]+1
    if(string[i]=="RO"):
        vet[3]=vet[3]+1
    if(string[i]=="RR"):
        vet[4]=vet[4]+1


print(max(vet))
print(vet)