num = int(input("digite o valor de num: "))
cont = 0

while num != -1:
	if num >= 51 and num <= 75:
		cont += 1
	num = int(input("digite o valor de num: "))
print(cont)