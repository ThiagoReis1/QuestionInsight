num = int(input())
cont = 0

while num != -1:
	if num >= 100 and num <= 199:
		cont += 1
	num = int(input())
		
print(cont)