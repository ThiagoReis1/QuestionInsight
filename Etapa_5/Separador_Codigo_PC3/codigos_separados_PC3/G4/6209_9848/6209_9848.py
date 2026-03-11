num = int(input())
erro = 0

while num != -1:
	if num >= 76 and num <= 100:
		erro = erro + 1
	num = int(input())
print(erro)