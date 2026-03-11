from numpy import*
estado = input(" digite aqui:  ").split(',')

d = zeros(5,dtype)

for i in range(size (estado)):	
	if estado[i]=="AM":
		d[0] = d[0]+1
	elif estado[i] == "PE":
		d[1] = d[1]+1
	elif estado[i] == "MG":
		d[2] = d[2]+1
	elif estado[i]=="SP":
		d[3] = d[3]+1
	elif estado[i]=="RS":
		d[4] = d[4]+1
print(max(d))		
		
print(d)		
		
		