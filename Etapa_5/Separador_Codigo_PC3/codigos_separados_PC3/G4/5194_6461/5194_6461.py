cl = input("Classisficacao(A ou B): ").upper()
vp = float(input("valor a ser pago: "))

if cl == "A" :
	vf = vp - (vp * 0.22) 
	print("Classe: Jounin")
else:
	vf = vp - (vp * 0.15)
	print("Classe: Chunin")
print(round(vf, 2))	