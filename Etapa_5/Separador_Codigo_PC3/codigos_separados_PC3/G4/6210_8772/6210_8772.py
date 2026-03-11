n = int(input())
cont = 0

while n != -1:
	if 35 <= n <= 95:
		cont = cont + 1
	n = int(input())	
print(cont)