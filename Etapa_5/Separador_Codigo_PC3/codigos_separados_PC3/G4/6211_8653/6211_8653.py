num = int(input())
cont = 0

while num >= 0:
	if num >= 100 and num <= 199:
		cont = cont + 1
		num = int(input())
	else: num = int(input())
print(cont)
	
