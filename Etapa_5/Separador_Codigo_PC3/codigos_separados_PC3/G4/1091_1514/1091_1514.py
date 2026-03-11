# Mayume Ihara Lima Rodrigues - 21602330
# Avaliacao 2
# Exercicio 2
# 14 / 07/ 2016

num = int(input("digite um numero: "))
a1 = num // 100
a2 = num % 100
x = (a1 + a2) ** 2

if(num == x):
		print(x, "atende a propriedade")
else:
		print(x)