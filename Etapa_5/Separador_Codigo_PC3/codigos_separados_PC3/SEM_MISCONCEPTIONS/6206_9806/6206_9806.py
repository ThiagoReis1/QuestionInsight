num = int(input("num: "))
contadora = 0
while num != -1:
	if 0<= num <= 25:
		contadora = contadora + 1
	num = int(input("num: "))
print(contadora)