peso = float(input("Insira o peso: "))
altura = float(input("Insira a altura: "))
IMC = peso / (altura) ** 2
if(IMC < 18.5):
	print("abaixo do peso")
elif(18.5 <= IMC < 25):
	print("normal")
if(25 <= IMC < 30):
	print("acima do peso")
elif(IMC >= 30):
	print("obeso")
