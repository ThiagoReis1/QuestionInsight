idade = int(input("idade: "))

total = 0

if idade < 12:
	total = 20 + 1.25
	print(round(total, 2))
	
elif idade == 12:
	total = 20 + 2.25
	print(round(total, 2))
	
else:
	total = 20 + 3.25
	print(round(total, 2))