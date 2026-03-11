t=int(input("Quantos tomates quer: "))

if t >= 4:
	total= t*0.55
	print(round(total,2))
else:
	total= t*0.75
	print(round(total,2))
	