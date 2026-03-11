from math import*
p = float(input("Digite o peso:"))
a = float(input("Digite a altura:"))
imc = p/((a)**2)
if (imc < 18.5):
	print ("abaixo do peso")
elif (imc >= 18.5 and imc < 25):
	print ("normal")
elif (imc <= 25 or imc < 30):
	print ("acima do peso")
elif (imc >= 30):
	print ("obeso")