num = int(input())

cont = 0

while num != -1:
	if 35 <= num and num <= 95:
		cont += 1
	num = int(input())
	
print(cont)