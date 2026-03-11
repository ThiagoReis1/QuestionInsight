from numpy import*
cod=input("Codigo das cores de cabelo:").split(',')
m=size(cod)
#Variaveis Contadoras
v=0
P=0
C=0
R=0
L=0
B=0
#Fazendo contagens
for i in range(m):
	if(cod[i]=="P"):
		P=P+1
	elif(cod[i]=="C"):
		C=C+1
	elif(cod[i]=="R"):
		R=R+1
	elif(cod[i]=="L"):
		L=L+1
	elif(cod[i]=="B"):
		B=B+1
#Criando um vetor com a quantidade de entradas equivalente as variaveis
vet=zeros(5,dtype=int)
#Fazendo a substituicao das variaveis pelas entradas
vet[0]=P
vet[1]=C
vet[2]=R
vet[3]=L
vet[4]=B
#Impressao
print(max(vet))
print(vet)