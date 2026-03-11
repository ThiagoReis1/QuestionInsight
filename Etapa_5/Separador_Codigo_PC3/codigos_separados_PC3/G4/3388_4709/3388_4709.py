var1 = input("Unidade de medida:")
var2 = float(input("Valor da medida:"))

if (var1=="W"):
	print(round(3.41214*var2, 2))
else:
	print(round(var2/3.41214, 2))
	