x = 0
i = 0
cont = 0

while x >= 0:
	x = int(input())
	if x >= 0 and x <= 25:
		cont = cont + i
		i += 1
		
print(i)