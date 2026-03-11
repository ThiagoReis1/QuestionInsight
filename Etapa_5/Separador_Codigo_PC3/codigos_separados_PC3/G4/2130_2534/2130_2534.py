from numpy import*
N = array(eval(input("Nota: ")))

Mf = (N[0] * 3.0 + N[1] * 2.0 + N[2] * 2.0 + N[3] * 3.0) / 10.0

print(round(Mf, 2))
if(Mf >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")