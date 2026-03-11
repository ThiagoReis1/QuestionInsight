from numpy import*
m = array(eval(input("TIPO DE MAGIA: ")))
n = array(eval(input("NÍVEL DO MAG0: ")))

i=0
soma = 0

while(i<size(m)):
	if(n[i] == "GELO"):
		soma += (2*(n[i]))
	if(n[i] == "FOGO"):
		soma += (3*(n[i]))
	if(n[i] == "CHOQUE"):
		soma += (4*(n[i]))
	if(n[i] == "CONJURACAO"):
		soma += (8*(n[i]))
	if(n[i] == "ILUSAO"):
		soma += (10*(n[i]))
	i = i + 1

print(soma)