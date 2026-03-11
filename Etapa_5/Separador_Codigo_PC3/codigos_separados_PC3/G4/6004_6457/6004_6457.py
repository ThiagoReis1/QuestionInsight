num = int(input("Digite o numero de tomates comprados: "))

if num >= 4:
	x = num * 0.55
else:
	x = num * 0.75
	
print(round(x, 2))