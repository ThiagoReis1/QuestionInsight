num = int(input("Digite o numero: "))
n100 = num// 1000
reston100 = num % 1000
propriedades = (n100 - reston100) ** 2
if (propriedades == num):
	print(propriedades, "atende a propriedade")
else:
	print(propriedades)
	
