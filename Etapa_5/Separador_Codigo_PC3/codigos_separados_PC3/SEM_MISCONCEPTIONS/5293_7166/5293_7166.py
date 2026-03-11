num = int(input("Digite o numero: "))
cont1 = 0   #total de numeros
cont2 = 0   #porcentagem de pares 

while(num != 0):
	cont1 = cont1 + 1
	if(num%2 == 0):
		cont2 = cont2 + 1
	num = int(input("digite o numero: "))
print(cont1)
print(round((cont2/cont1*100),2))