peso = float(input("peso: "))
altura = float(input("altura: "))

imc = ((peso)/(altura**2))

if(imc<18.5):
	print("abaixo do peso ")
else:
	if(18.5<=imc<25):
		print("normal ")
	else:
		if(25<=imc<30):
			print("acima do peso ")
		else:
			print("obeso")
	
	



