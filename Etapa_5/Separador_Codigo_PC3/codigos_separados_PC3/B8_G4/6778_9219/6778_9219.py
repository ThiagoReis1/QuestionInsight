n = int(input("Ano de nascimento: "))
p = input("(P/J)")

if (2023 - n >= 21) and ((p == "B") or (p == "b")):
	print("sim")
	print((2023 - n) - 21)
elif (2023 - n < 21) and ((p == "B") or (p == "b")):
	print("nao")
	print(21 -(2023-n))
elif (2023 - n >= 20) and ((p == "J") or (p == "j")):
	print("sim")
	print((2023 - n) - 20)
elif (2023 - n< 20) and ((p == "J") or (p== "j")):
	print("nao")
	print(20 - (2023-n))