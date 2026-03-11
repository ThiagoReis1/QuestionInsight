fatia = input("Bolo ou croissant?(B para bolo ou C para croissant): ")
qf = int(input("Quantidade de fatias: "))
qc = int(input("Quantidade de capuccinos: "))

if (fatia.upper() == "B"):
	conta = (qf*3) + (qc*5.5)
elif (fatia.upper() == "C"):
	conta = (qf*6) + (qc*5.5)
print(round(conta,2))