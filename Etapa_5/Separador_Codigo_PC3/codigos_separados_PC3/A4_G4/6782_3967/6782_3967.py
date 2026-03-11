nasc = int(input())
pais = input().upper()

id = 2023 - nasc

if pais == "B" or pais == "E":
	if pais == "B":
		if id < 18:
			p1 = "nao"
			p2 = 18 -id
		else:
			p1 = "sim"
			p2 = id - 18
	else:
		if id < 16:
			p1 = "nao"
			p2 = 16 - id
		else:
			p1 = "sim"
			p2 = id - 16
	print(p1)
	print(p2)
else:
	print("invalido")