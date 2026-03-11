p = float(input("peso: "))
h = float(input("altura: "))

from math import*

imc = p / h**2
#print("imc",imc)
if (imc < 18.5):
	print ("abaixo do peso")
elif (18.5 <= imc < 25):
	print ("normal")
elif (25 <= imc < 30):
	print ("acima do peso")
elif (imc >= 30):
	print ("obeso")
