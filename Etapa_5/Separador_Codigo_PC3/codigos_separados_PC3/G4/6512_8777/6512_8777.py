# faça seu código aqui!
qDD = int(input("quantidade de DD:"))
DD = 32.90
vt = DD*qDD 
vtd = qDD*DD*(20/100)*4


if qDD <= 3:
	print(round(vt, 2))
else:
	print(round(vtd, 2))