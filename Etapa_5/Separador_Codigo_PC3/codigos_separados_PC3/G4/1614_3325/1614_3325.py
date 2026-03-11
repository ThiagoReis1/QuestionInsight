from numpy import*
nome = array(eval(input("digite nome: ")))
q = array(eval(input("digite quant: ")))
i = 0
a = 0
while(i<size(nome)):
	if (nome[i] == "BANANA"):
		a = a + (0.97*q[i])
	if (nome[i] == "BIFE"):
		a = a + (2.95*q[i])
	if (nome[i] == "FEIJOADA"):
		a = a + (1.27*q[i])
	if (nome[i] == "OMELETE"):
		a = a + (1.04*q[i])
	if (nome[i] == "TOMATE"):
		a = a + (0.2*q[i])
	i = i + 1
print(round(a,2))
	