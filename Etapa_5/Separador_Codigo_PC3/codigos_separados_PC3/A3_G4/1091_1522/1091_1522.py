# Ana Regina dos Santos da Silva - Mat. 21603561
# 07/07/2016
# Exercicio 2

num = int(input("Digite o num: "))

a = num // 1000
ra = num % 1000
	
b = ra // 100
rb = ra % 100
	
c = rb // 10
rc = rb % 10
	
d = rb // 1

if (num == ((a + b) + (c + d)) ** 2):
	print(num, "atende a propriedade")
	
else:
	print(((a + b) + (c + d)) ** 2)
	
	
	
