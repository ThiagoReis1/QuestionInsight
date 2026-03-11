cod=input("qual o codigo:")
sal=float(input("qual o salario atual:"))


if cod=="101":
	f1=(sal/100)*10
	f2=sal+f1
	print(round(f2,2))
	print("Aumento de 10 por cento")

else:
	f3=(sal/100)*30
	f4=f3+sal
	print(round(f4,2))
	print("Aumento de 30 por cento")

