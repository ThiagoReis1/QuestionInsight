peso = float(input("peso da pessoa: "))
altura = float(input("altura da pessoa: "))
IMC = peso/(altura**2)
if(IMC < 18.5):
	print("abaixo do peso")
elif(IMC >= 18.5) and (IMC < 25):
	print("normal")
elif(IMC >= 25) and (IMC < 30):
	print("acima do peso")
elif(IMC >= 30):
	print("obeso")
else:
	print("dados invalidos")