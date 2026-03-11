num= int(input("insira um numero de 4 digitos"))
num1= num//100
num2= num%100
condicao=(num1+num2)**2==num
if condicao:
	print(num)
	print("atende")
else:
	print(num)
	print("nao atende")