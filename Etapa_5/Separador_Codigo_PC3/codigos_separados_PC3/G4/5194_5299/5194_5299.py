M = input("")
V = float(input())

if (M == "A"):
	C =  V - V*0.22
	print("Classe: Jounin")
	print(round(C,2))
else:
	J =  V - V*0.15
	print("Classe: Chunin")
	print(round(J,2))