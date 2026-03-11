num=3 #variavel aleatoria
quant= 0

while num != -1:
	num= int(input("Insira um valor:"))
	if 101 <= num <= 201:
		quant= quant + 1
	
print(quant)