n = int(input())
contador = 0
while n != -1:
	if n >= 35 and n <= 95:
		contador += 1
		n = int(input())
	else:
		n = int(input())

print(contador)
