va = int(input("Votos ambrosio: "))
vd = int(input("Votos demelza: "))

x = va + vd
vap = (va / x) * 100
vdp = (vd / x) * 100

if (va > vd):
	print("Ambrosio Rutra")
	print(round(vap, 2))
if (vd > va):
	print("Demelza Olecram")
	print(round(vdp, 2))