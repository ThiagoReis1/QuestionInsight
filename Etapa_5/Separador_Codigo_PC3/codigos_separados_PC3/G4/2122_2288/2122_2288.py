from numpy import*

v = array(eval(input()))

n0 = v[0]
n1 = v[1]
n2 = v[2]

nf = (2*n0 + 3*n1 + 5*n2)/10

print(round(nf, 2))

if nf >= 5:
	print("APROVADO")
else:
	print("REPROVADO")