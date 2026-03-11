num = float(input(""))
num1 = float(input(""))
num2 = float(input(""))
num3 = float(input(""))

cont = (num + num1 + num2 + num3)/4

if cont >= 5.0: 
	print(round(cont, 2))
	print("Aprovacao")
else: 
	print(round(cont, 2))
	print("Reprovacao")
