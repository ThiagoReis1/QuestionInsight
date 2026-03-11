# faça seu código aqui!
id = int(input("Idade: "))

if id<12:
	total = 20+1.25
elif id == 12:
	total = 20+2.25
elif id>12:
	total = 20+3.25
print(round(total,2))