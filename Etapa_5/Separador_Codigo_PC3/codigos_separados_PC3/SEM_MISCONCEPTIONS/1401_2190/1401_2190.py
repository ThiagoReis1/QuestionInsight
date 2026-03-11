ataque = input("")
quantidade = int(input())

if (ataque.lower == "MARITIMO"):
	print("Drogon")
	print(int(quantidade//150 + 1))
else:
	print("Viserion")
	print(int(quantidade//40 + 1))