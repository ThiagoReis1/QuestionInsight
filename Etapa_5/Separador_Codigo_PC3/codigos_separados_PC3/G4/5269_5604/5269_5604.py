k=0
i=0
n=int(input("Digite um numero:"))
while(n!=0 and n>0):
	if(n%3 == 0):
		k= k+1
		i=i+1
	else:
		i=i+1
	n=int(input("outro numero: "))

porcentagem= (k/i)*100
print(i)
print(round(porcentagem,2))
		
		
		