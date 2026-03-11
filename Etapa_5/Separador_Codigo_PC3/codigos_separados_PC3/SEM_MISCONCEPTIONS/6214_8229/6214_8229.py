contador = 0 

while True:
	numero = int(input("Digite um numero: "))
	
	if numero < 0:
		break
	
	if 45<= numero <= 150: 
		contador += 1
		
print(contador)
		