from numpy import *
s = input("Informe a string de nacionalidades: ")
vet = zeros(5, dtype=int)
s=s.split(',')
for i in range(size(s)):
	if s[i]=="AR":
		vet[0]=vet[0]+1
	elif s[i]=="BR":
		vet[1]=vet[1]+1
	elif s[i]=="CL":
		vet[2]=vet[2]+1
	elif s[i]=="CO":
		vet[3]=vet[3]+1
	elif s[i]=="UY":
		vet[4]=vet[4]+1
print(max(vet))
print(vet)