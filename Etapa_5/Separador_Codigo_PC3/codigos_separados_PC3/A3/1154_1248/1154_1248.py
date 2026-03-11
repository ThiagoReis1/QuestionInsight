numero = float(input("numero: "))
taxa = input("taxa: ")
copias = input("copias: ")
copia_ml = 0
semana = 1
while (numero >= 10000):
	numero = numero + (numero * taxa) 
	copias  = copias  + numero
	semana = copias + 1
	print(semana)
	
	

	
	