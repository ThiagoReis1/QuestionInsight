from numpy import *
vet = input("Informe a secao: ").upper()
i = 0
t = 0
cont = 0
contl = 0
contp = 0
while i<len(vet):
	if(vet[i]=="A"):
		cont = cont+1
	elif(vet[i]=="L"):
		contl=contl+1
	elif(vet[i]=="P"):
		contp = contp+1
	i = i+1

t = (cont*16.75)+(contl*4.60)+(contp*2.85)
print(round(t,2),cont,contl,contp)
		