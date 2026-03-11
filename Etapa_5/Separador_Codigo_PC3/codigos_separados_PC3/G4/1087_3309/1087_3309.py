p1 = float(input("insira nota da p1: "))
p2 = float(input("insira nota da p2: "))
p3 = float(input("insira nota da p3: "))
p4 = float(input("insira nota da p4: "))

mA = round(((p1 + p2 + p3 + p4)/4),2)

if (mA >= 7.0):
	print(mA)
	print("Aprovado")
else:
	print(mA)
	print("Reprovado")