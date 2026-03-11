data = eval(str(input("Array:")))

taxa_acrescimo = data[0]
i = 1

acumulador = 0

for x in data[1:]:
	if x >=taxa_acrescimo:
		print(i)
		acumulador = acumulador + 1
	i = i + 1
	
print(acumulador)