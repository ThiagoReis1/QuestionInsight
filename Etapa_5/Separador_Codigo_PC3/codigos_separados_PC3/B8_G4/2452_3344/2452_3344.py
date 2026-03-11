
a = float(input("Peso: "))
b = float(input("Altura: "))

IMC = a/b**2

if(IMC<18.5):
	print("abaixo do peso")
elif(18.5<IMC and IMC<25):
	print("normal")
elif(25<=IMC and IMC<30):
	print("acima do peso")
elif(IMC>=30):
	print("obeso")	