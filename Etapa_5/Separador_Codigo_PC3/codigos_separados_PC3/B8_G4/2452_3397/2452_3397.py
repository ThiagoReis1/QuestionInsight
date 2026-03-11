p = float(input("Digite o peso: "))
a = float(input("Digite a altura: "))
IMC = p/(a**2)

if(IMC < 18.5):
	print("abaixo do peso")
elif(18.5 <= IMC < 25):
	print("normal")
elif(25 <= IMC < 30):
	print("acima do peso")
elif(IMC >= 30):
	print("obeso")
   
