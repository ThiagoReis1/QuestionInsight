from numpy import*

v = array(eval(input("vetor: ")))

nf = (v[0] * 2.0 + v[1] * 3.0 + v[2] * 5.0) / 10.0
print(round(nf,2))
if (nf >= 5.0):
	msg = "APROVADO"
else:
	msg = "REPROVADO"
print(msg)

