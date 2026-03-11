from numpy import*
vet = (input("Digite:")).split(',')
r = zeros(5, dtype=int)



i = 0

for cont in vet:
	
	if(cont == 'CHN'):
		r[0] = r[0] + 1
		
		
	elif(cont == 'JPN'):
		r[1] = r[1] + 1
		
	elif(cont == 'KOR'):
		r[2] = r[2] + 1
		
	elif(cont == 'MGL'):
		r[3] = r[3] + 1
		
	elif(cont == 'THA'):
		r[4] = r[4] + 1
		

print(r)		
		
	