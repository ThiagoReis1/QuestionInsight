a = int(input(""))
p = input("").upper()
d = 2023 - a
if (p == 'B' and d >= 21) or (p == 'J' and d >= 20):
	print("sim")
	if (p == 'B'):
		F = d - 21
		print(F)
	else:
		F = d - 20
		print(F)
elif(p == 'J' and d < 20) or (p == 'B' and d < 21):
	print("nao")
	if (p == 'B'):
		i = 21 - d
		print(i)
	else:
		i = 20 - d
		print(i)
	
else:
	print("invalido")

