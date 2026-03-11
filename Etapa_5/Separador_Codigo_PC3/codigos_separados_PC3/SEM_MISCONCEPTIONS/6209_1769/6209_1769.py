valor = int(input())
cont = 0

while(valor >= 0):
	if(valor >= 76 and valor <= 100):
		cont = cont + 1
	valor = int(input())
	
print(cont)