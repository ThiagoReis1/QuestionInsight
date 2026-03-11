#Universidade Federal do Amazonas 
#Laís Amorim Reis - 21602327

n = int(input("n: "))
numerador = 1
denominador = 1
i = 1
var = 0
while(i<=n):
	if(i==1):
		var = 0.2
	elif(i%2==0):
		var = var - ((numerador**2)/(4+denominador))
	else:
		var = var + ((numerador**2)/(4+denominador))
	i = i+1
	numerador = numerador + 1
	denominador = denominador + 2
print(round(var,8))
	
