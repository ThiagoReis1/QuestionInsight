#Instituto de computação-UFAM
#Suenne Renata Lima Fernandes- 21602342
#AV02- Exercício 02

numero = int(input("Digite um número:"))
a = numero // 100
b = numero % 100
ab = ((a**2)+(b**2))
if (numero == ab):
	print (numero, "atende a propriedade")
else:
	print (((a**2)+(b**2)))