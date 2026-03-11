a = int(input("a: "))
p = input("p: ").upper()
i = 2023 - a

if p == "B":
	if i >= 18:
		mi = i - 18
		print("sim")
		print(mi)
	else:
		qf = 18 - i
		print("nao")
		print(qf)
elif p == "J":
	if i >= 16:
		mi = i - 16
		print("sim")
		print(mi)
	else: 
		qf = 16 - i
		print("nao")
		print(qf)
		
else:
	print("invalido")