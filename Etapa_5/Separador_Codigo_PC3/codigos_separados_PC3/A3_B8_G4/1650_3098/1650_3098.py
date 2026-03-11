##lembrar que é uma string
##codigos do cabelo é armazenados por virgulas
  #saidas#
#maior numero de pessoas com a mesma cor de cabelo
#ele quer a quantidade de clientes de cada tipo(checar a ordem no final)
from numpy import*
string=input("siglas dos clientes:   ")
vet = string.split(",")#transformei para vetor
tvet=size(vet)
#criaçao de contadoras para o cabelo
p = 0
c = 0
r = 0
l = 0
b = 0
k = 0#isso é para o vetor saida
#meu vetor saida
saida = zeros(5,dtype=int)
#criaçao do meu laço para atribuiçao e checagem
for i in range(size(vet)):
	if(vet[i]=="P"):
		p = p + 1	
	elif(vet[i]=="C"):
		c = c + 1
	elif(vet[i]=="R"):
		r = r + 1
	elif(vet[i]=="L"):
		l = l + 1
	elif(vet[i]=="B"):
		b = b + 1
saida[0]=p
saida[1]=c
saida[2]=r	
saida[3]=l
saida[4]=b
print(max(saida))
print(saida)
	