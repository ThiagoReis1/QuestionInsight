from math import *
peso = float(input("Digite seu peso:"))
alt = float(input("Digite sua altura:"))
altura = float(alt*alt)
imc = float(peso/altura)
if(imc<18.5):
	print("abaixo do peso")
elif(imc>=18.5) and (imc<25):
	print("normal")
elif(imc>=25) and (imc<30):
	print("acima do peso")
elif(imc>=30):
	print("obeso")
