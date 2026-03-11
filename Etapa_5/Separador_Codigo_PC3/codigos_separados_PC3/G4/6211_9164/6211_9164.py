num = int(input())

cont = 0

while num != -1:
	if 100 <= num <= 199:
		cont += 1
	num = int(input())
	
print(cont)