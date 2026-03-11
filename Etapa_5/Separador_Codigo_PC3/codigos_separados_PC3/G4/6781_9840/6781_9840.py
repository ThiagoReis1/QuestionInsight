n = int(input("ano de nascimeneto:"))
p = input("insira B ou E:").upper()
i=2023-n
if p=='E':
	if i>=18:
		print("sim")
		print(i-18)
	else:
		print("nao")
		print(18-i)
elif p=="B":
	if i>=21:
		print("sim")
		print(i-21)
	else:
		print("nao")
		print(21-i)
else:
	print("invalido")