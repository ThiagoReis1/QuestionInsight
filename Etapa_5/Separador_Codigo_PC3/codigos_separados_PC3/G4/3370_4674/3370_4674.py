var1 = input("Unidade de medida")
var2 = float(input("Valor da medida:"))

if (var1=="C"):
  print(round(0.393701*var2, 2))
else:
	print(round(var2/0.393701, 2))