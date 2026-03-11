peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

if(imc < 18.5):
	print("abaixo do peso")
	
elif(18.5 <= imc < 25):
	print("normal")
	
elif(25 <= imc <= 30):
	print("acima do peso")
	
elif(imc > 30):
	print("obeso")