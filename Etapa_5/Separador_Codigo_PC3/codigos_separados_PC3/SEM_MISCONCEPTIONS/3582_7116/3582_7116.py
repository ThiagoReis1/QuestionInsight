from numpy import*

cust = array(eval(input(": ")))
quant = size(cust)
cont = 0

for i in range (quant):
	if cust[i] > 160.0:
		cont = cont + (cust[i] - 25)
	else:
		cont = cont + cust[i]
print(cont)