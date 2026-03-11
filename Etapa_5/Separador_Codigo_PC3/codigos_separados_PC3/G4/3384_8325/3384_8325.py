unit=input("qual a unidade em que a medida esta: O para oncas ou K para quilogramas: ")
vm= float(input("qual o valor da medida: "))

if (unit.upper() == "K"):
	print(round(35.274*vm,2))
else:
	print(round(vm/35.274,2))
