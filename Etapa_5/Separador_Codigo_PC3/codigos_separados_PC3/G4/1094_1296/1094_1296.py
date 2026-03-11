# Phillip de Sousa Silva
# Eng. Mecanica, AV 02, Ex 02
# 30/06/16

num = int(input("Digite o valor"))

a=num//1000
resto100=num%1000

e=(a+resto100)**2

if (num==e):
  	print(e,"atende a propriedade")
else:
	print(e)
