UM = input("Unidade a ser comvetida:(A ou H) ")
VM = float(input("Valor da medida: "))

if UM.upper() == "A":
	print(round(VM/2.47105, 2))
else:
	print(round(VM*2.47105, 2))