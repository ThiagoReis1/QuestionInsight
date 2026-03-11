num = int(input())
cont = 0
while (num != -1):
	if 26 <= num <= 50:
		cont += 1
	num = int(input())
print(cont)