intervalo = int(input("Digite o numero: "))
contador = 0

while(intervalo != -1):
	if(26 <= intervalo <= 50):
		contador = contador +1
	intervalo = int(input("Digite o numero: "))
print(contador)