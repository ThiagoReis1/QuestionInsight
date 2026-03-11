from numpy import*
n = array(eval(input("notas: ")))
nf = (n[0]*5 + n[1]*3 + n[2]*2)/10
if (nf >= 5):
	print(round(nf,2))
	print("APROVADO")
else:
	print(round(nf,2))
	print("REPROVADO")