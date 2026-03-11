num1=int(input("Qual o valor da soma?"))
num2=num1//2550
num3=num1%2500
soma=((num2+num3)**2)

if (soma == num1):
	print(num1,"atende a propriedade")
else:
	print(soma)