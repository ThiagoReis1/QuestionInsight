from numpy import*
p = str (array([ARROZ,FANTA,BIS]))#array (eval(input("produtos: ")))
q = array ([1,3,2])#array (eval(input("quantidades: ")))

preco = array([1.25,2.6,1.8,0.85,3.2])

i = 0
valor = 0

while (i < size(p)):
	if (p[i]=="ARROZ"):
		valor = valor + (preco(i)*q(i))
		i = i + 1
	elif (p[i]=="FEIJAO"):
		valor = valor + (preco(i)*q(i))
		i = i + 1
	elif (p(i)=="BIS"):
		valor = valor + (preco(i)*q(i))
		i = i + 1
	elif (p(i)=="MIOJO"):
		valor = valor + (preco(i)*q(i))
		i = i + 1
	elif (p(i)=="FANTA"):
		valor = valor + (preco(i)*q(i))
		i = i + 1
print (round(valor,2))