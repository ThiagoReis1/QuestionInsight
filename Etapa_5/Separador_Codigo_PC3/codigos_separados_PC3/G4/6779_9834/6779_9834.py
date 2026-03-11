i = int(input("digite:"))
p = input("(B)para brasil e (J) para japao:").upper()

if (p == "B") and (2023 - i>= 18):
	print("sim")
	print((i+18)- 2023)
elif (p == "B") and (2023 - i <= 18):
	print("nao")
	print((i+18)- 2023)
elif (p=="J") and (2023 -i >=16):
	print("sim")
	print(2023-(i+16))
elif (p=="J") and(2023 - i <= 16):
	print("nao")
	print(2023-(i+16))
else:
	print("invalido")