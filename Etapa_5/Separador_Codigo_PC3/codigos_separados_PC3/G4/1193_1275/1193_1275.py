from numpy import*

valor = array (eval(input("temperatura ambiente:")))
E = array(dtype = float )
i = 0
k = 0

while (i < size (valor)):
	if (valor[i] < -100 ):
		E[k] == valor[i]
		k = k + 1
	i = i + 1

print(E)