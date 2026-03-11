intervalo = int(input("Digite o numero: "))
contadora = 0

while(intervalo != -1):
	if(0 <= intervalo <= 25):
		contadora = contadora +1
	intervalo = int(input("Digite o numero: "))
print(contadora)