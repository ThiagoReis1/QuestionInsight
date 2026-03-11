ano = int(input())
pais = input().upper()

	
tt = 2023 - ano
if pais == "R" and tt >= 18:
	print("sim")
	print(tt - 18)
	
elif pais == "R" and tt < 18:
	print("nao")
	print(tt - 18)

elif pais == "B" and tt < 21:
	print("nao")
	print(21 -tt)
	
elif pais == "B" and tt >= 21:
	print("sim")
	print(21-tt)

else:
	print("invalido")