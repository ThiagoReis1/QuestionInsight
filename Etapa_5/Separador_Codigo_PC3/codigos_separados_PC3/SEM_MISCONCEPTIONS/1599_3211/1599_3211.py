from numpy import*
compras = array(eval(input("precos: ")))
e = size(compras)
comd = zeros(e)
for i in range(e):
	if(compras[i]>80):
		comd[i] = compras[i]*(85/100)
	else:
		comd[i] = compras[i]
print(round(sum(comd), 2))