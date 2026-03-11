#Universidade Federal do Amazonas
#Aluna: Ingrid de Lira Lima
#Exercicio: 01



from numpy import*
vetor= array(eval(input("digite as distâncias: ")))

x= 98.48
i=0
j=0

while i< size(vetor):
	if vetor[i]< x:
		j= j+1
	i=i+1

print(x)
print(j)
	




