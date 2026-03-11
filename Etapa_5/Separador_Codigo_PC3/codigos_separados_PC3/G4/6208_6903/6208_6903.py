num = int(input("Insira um inteiro: "))
c = 0
while num != -1:
	if num >= 51 and num <= 75:
		c = c +1
	num = int(input("Insira um numero: "))
print(c)