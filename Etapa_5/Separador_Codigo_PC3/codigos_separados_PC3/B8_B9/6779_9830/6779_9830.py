a = int(input("digite o ano do seu nascimento: "))
b = input("Digite (B) para brasil e (J) para japao: ").upper()

if b == 'B':
	total = 2023 - a
	if total < 18:
		total_2 = 18 - total
		print("nao")
		print(total_2)
	elif total >= 18:
		total_2 = total - 18
		print("sim")
		print(total_2)

		
elif b == 'J':
	total = 2023 - a
	if total < 16:
		total_2 = 16 - total
		print("nao")
		print(total_2)
	elif total >= 16:
		total_2 = total - 16
		print("sim")
		print(total_2)
		
		
else:
	print("invalido")