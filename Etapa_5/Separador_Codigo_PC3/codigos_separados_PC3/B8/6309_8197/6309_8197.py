from numpy import *

produtos = input("Digite o produto desejado: ").upper()
i = 0
total = 0
quantidade_h = 0
quantidade_c = 0
quantidade_l = 0

while (i < len(produtos)):
	if (produtos[i] == "H"):
		quantidade_h = quantidade_h + 1
		total = total + 5.40
	elif (produtos[i] == "C"):
		quantidade_c = quantidade_c + 1
		total = total + 8.95
	elif (produtos[i] == "L"):
		quantidade_l = quantidade_l + 1
		total = total + 4.50
	i = i + 1
print(round(total, 2), quantidade_h, quantidade_c, quantidade_l)