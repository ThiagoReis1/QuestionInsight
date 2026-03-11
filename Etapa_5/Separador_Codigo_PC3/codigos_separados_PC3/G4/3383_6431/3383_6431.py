x = input("Digite a unidade:").upper()
v = float(input("Digite o valor da medida:"))
#vm = v * 2.20462

if x == "L":
   vm = v / 2.20462
   print(round(vm, 2))

	
else:
	vm = v * 2.20462
	print(round(vm, 2))	