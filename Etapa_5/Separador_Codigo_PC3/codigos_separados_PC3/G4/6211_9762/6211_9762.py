x = int(input())
cont = 0

while x != -1:
	if 100 <= x <= 199:
		cont = cont + 1
	x = int(input())
print(cont)