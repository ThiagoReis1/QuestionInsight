idade = int(input("idade: "))

cont1 = 0
cont2 = 0

while idade != -1:
	if 0 < idade < 18:
		cont2 += 1
	cont1 += 1
	idade = int(input("idade: "))
percentual = (cont2 / cont1) * 100
print(cont1)
print(round(percentual, 2))