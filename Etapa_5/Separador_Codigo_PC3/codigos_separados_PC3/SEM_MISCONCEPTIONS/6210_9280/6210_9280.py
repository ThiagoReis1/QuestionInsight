intervalo = int(input("digite o numero: "))
contador = 0 

while(intervalo != -1):
	if(35 <= intervalo <= 95):
		contador = contador +1
	intervalo = int(input("digit o numero: "))
print(contador)