vtotal = float(input("Qual o valor total da compra? "))
cod = input("Qual o codigo? ")
d = vtotal * 0.88
p = vtotal * 0.88
c1 = vtotal
c2 = vtotal * 1.07
if(cod == "D"):
	x = vtotal * 0.88
	print(round(x, 2))
elif(cod == "P"):
	x = vtotal *0.88
	print(round(x, 2))
elif(cod == "C1"):
	x = vtotal
	print(round(x, 2))
elif(cod == "C2"):
	x = vtotal * 1.07
	print(round(x, 2))