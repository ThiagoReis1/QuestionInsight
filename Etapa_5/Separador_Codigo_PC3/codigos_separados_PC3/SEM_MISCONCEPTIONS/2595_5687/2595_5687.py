
data = eval(str(input("Array: ")))
taxa_reducao = data[0] * (-1)
i = 1

acumulador = 0

for x in data[1:]:
	if x <= taxa_reducao:
		print(i)
		acumulador = acumulador + 1
	i = i + 1
print(acumulador)