from numpy import*

v = array(input("Nome do Produto: ").upper())
v = array(["ARROZ","FEIJAO","BIS","MIOJO","FANTA"])
q = array(eval(input("Quantidade: ")))
i = 0 
v[0] = 1.25
v[1] = 2.60
v[2] = 1.80
v[3] = 0.85
v[4] = 3.20

if (q[0] == v[0]):
	total = q * v

print(round(total, 2))