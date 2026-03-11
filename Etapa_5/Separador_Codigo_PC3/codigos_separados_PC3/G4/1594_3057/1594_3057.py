from numpy import*
d = array (eval(input("Informe os danos na sequencia: ")))
i = 0
a = 1
cont = 0
while (i < size(d)):
	cont= cont + d[i] * a
	a = a + 1
	i = i + 1
	
print (cont)