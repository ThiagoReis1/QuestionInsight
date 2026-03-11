fatia = input("Informe qual fatia deseja: ")
q = int(input("Informe a quantidade que deseja: "))
qc = int(input("Quantidade de cappucinos: "))

if (fatia.upper() == "B"):
	v1 = (q * 5.00) + (qc * 7.50)
	print(v1)

if (fatia.upper() == "S"):
	v2 = (q * 4.00) + (qc * 7.50)
	print(v2)