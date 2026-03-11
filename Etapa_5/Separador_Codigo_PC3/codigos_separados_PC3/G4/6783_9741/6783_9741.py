ano = int(input("ano:"))
p = input("pais:")

if p.upper() == "B":
	a = 2023 - ano
	if a>=18:
		print("sim")
		b = a - 18
		print(b)
	else:
		print("nao")
		c = 18 - a
		print(c)
		
elif p.upper()  == "E":
	
	a = 2023 - ano 
	if a>= 16:
		print("sim")
		b = a - 18
		print(b)
	else:
		print("nao")
		c = 16 - a
		print(c)
		
else:
	print("invalido")