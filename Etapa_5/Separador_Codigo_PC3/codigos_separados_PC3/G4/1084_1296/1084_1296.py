# Phillip de Sousa Silva
# Eng. Mecanica, AV 02, Ex 01
# 30/06/16

num1 = float(input("Digite o valor"))
num2 = float(input("Digite o valor"))
num3 = float(input("Digite o valor"))
num4 = float(input("Digite o valor"))

a = (num1+num2+num3+num4)/4

if (a>=6):
	print(round(a,1))
	print("Aprovado")

else:
	print(round(a,1))
	print("Reprovado")
