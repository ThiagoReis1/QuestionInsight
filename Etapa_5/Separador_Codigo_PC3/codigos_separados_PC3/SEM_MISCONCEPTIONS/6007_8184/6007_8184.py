m = int(input("Leia o numero de espigas de milho: "))
if m < 5:
	milho = m*1.85
	print(round(milho, 2))
else:
	milho= m*1.50
	print(round(milho,2))