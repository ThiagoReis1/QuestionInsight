n = int(input())
cont = 0

while n != -1:
	if n >= 26 and n <= 50:
		cont += 1
	n = int(input())
	
print(cont)