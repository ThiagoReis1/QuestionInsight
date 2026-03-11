a = int(input("ano de nascimento: "))
p = input("B ou E: ").upper()

i = 2023 - a 

if p == "B":
	if i >= 21:
		print("sim")
		print(i-21)
	else:
		print("nao")
		print(21-i)
elif p == "E":
	if i >= 18:
		print("sim")
		print(i-18)
	else:
		print("nao")
		print(18-i)
else:
	print("invalido")
	
		
		
	