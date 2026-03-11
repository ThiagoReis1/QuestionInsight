p=float(input())
a=float(input())


imc=(p/(a*2))
if(imc>=0):
	if (imc<18.5):
		print("abaixo do peso")
	if (imc>=18.5 and imc<25):
		print("normal")
	if (imc>=25 and imc<30):
		print("acima do peso")
	if (imc>=30):
		print("obeso")
