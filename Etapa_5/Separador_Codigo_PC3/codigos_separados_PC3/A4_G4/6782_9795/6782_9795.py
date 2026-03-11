ano = int(input("nascimento: "))
pais = input("B/E: ").upper()
id = 2023 - ano
 
if pais == "B":
	if id >= 18:
		print("sim")
		print(id-18)
	else:
		print("nao")
		print(18 -id)
elif pais == "E":
	if id >= 16:
		print("sim")
		print(id-16)
			
	else: 
		print("nao")
		print(16-id)
else:
	print("invalido")
