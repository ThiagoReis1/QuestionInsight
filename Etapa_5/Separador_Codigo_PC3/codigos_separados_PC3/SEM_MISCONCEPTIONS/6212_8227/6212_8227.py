contador_numeros_saudaveis = 0

while True:
	numero =int(input("digite um numero:"))
	
	if numero < 0:
		break
		
	if 26 <= numero <= 85:
		contador_numeros_saudaveis +=1
		
print( contador_numeros_saudaveis)		
