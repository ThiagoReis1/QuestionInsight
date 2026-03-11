contador = 0
while True: 
	num = int(input("numero:"))
	if num == -1:
		break
	if 100 <= num <= 199:
		contador += 1
print(contador)
		