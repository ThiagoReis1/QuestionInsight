# Rodrigo de Oliveira Brasil Ferreira - 21602328
# Prova 02
# 07 / 07 / 2016
# Engenharia Quimica

num = int(input("digite o numero desejado: "))
x1 = num // 1000
x2 = num % 1000
a = (x1 + x2) ** 2
if(a == (x1 + x2) ** 2):
	print(a)	
else: 
	
	print(a, "atende a propriedade")	
