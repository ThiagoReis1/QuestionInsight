from numpy import*
quant = array(eval(input()))
i = 0
v = zeros(5)
while(size(quant) > i):
	if(quant[i] == 'AC'):
		  am += 1
	elif(quant[i] == 'AM'):
		  ac += 1
	elif(quant[i] == 'PA'):
		  pa += 1
	elif(quant[i] == 'RO'):
		  ro += 1
	elif(quant[i] == 'RR'):
		  rr += 1
	i += 1
v[a] = v[am]
print(v)