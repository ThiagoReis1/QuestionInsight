a = int(input("Seu nascimento: "))
b = input("Coloque o pais:").upper()

total = 2023 - a
x = total - 18
y = total - 16

bb = 18 - total
jj = 16 - total

if b == "B":
	if total >= 18:
		print("sim")
		print(x)
	else:
		print("nao")
		print(bb)

elif b == "J":
	if total >= 16:
		print("sim")
		print(y)
	else:
		print("nao")
		print(jj)
else:
	print("invalido")
		
	
