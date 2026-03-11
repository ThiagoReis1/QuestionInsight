# Aluna: Lizandra Kamila Muniz de Andrade - 21553759
# Universidade Federal do Amazonas - UFAM
# 14/07/16
valor = int (input("digite um valor: "))
a = valor // 10000
restoa = valor % 10000
b = restoa // 100
restob = restoa % 100
c = restob % 100
X = ((a**3) + (b**3) + (c**3))
if (X==valor):
	print(X, "atende a propriedade")
else:
	print(X)