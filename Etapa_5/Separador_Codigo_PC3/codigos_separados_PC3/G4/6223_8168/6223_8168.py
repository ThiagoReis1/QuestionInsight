x=int(input("valor de x: "))
y=int(input("valor de y: "))
cont=0
soma=0

while(cont<=y):
	if(cont>=x and (cont%2)!=0):
		soma = soma +cont
	cont = cont+1
print(soma)