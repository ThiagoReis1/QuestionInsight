from numpy import*

vet = input().split(',')
vat = zeros(5, dtype=int)
be = 0
es = 0       
fr = 0    						
it = 0
pt = 0
maior = 0
for elemento in vet:

	if(elemento == 'BE'):
		vat[0] = vat[0] + 1
		be = be + 1
		
	elif(elemento == 'ES'):
		vat[1] = vat[1] + 1
		es = es +1
		
	elif(elemento == 'FR'):    
		vat[2] = vat[2] + 1
		fr = fr +1     
	elif(elemento == 'IT'):
		vat[3] = vat[3] + 1
		it = it +1
	elif(elemento == 'PT'):
		vat[4] = vat[4] + 1
		pt = pt +1
		
print(max(vat))
print(vat)