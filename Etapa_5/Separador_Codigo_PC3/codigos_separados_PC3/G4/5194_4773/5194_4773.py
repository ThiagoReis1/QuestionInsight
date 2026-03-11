cm = input("qual classe da missao: ")
vp = float(input("qual valor pago pela missao: "))

if cm == "B":
	print("Classe: Chunin")
	vf = vp - (0.15*vp)
	print(round(vf, 2))
else:
	print("Classe: Jounin")
	vf = vp - (0.22*vp)
	print(round(vf, 2))