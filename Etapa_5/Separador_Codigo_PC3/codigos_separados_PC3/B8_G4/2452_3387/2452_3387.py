p=float(input("peso:"))
a=float(input("altura:"))
imc=p/a**2
if	(imc<18.5):
	print("abaixo do peso")
elif(18.5<=imc<25):
	print("normal")
elif(25<=imc<30):
	print("acima do peso")
elif(imc>=30):
	print("obeso")


	