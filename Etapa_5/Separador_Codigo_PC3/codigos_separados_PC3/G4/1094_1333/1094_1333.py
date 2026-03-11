num1=int(input("Informe um valor:"))
num2=num1//1000
num3=num1%1000
soma=((num2+num3)**2)

if (soma == num1):
	print(num1, "atende a propriedade")
else:
	print(soma)