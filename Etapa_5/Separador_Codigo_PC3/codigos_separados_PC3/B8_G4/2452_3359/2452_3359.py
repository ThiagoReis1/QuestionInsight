a = float(input("digite o peso: "))
b = float(input("digite a altura: "))

imc = a / b ** 2 

if (imc < 18.5 or 18.5 <= imc < 25 or 25 <= imc < 30 or imc >= 30):
	if (imc < 18.5):
		print("abaixo do peso")
	elif (18.5 <= imc < 25):
		print("normal")
	elif (25 <= imc < 30):
		print("acima do peso")
	elif (imc >= 30):
		print("obeso")