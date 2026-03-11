lado = int(input())

cont = 1
cont1 = 0

while(lado != -1):
	lado = int(input())
	if (lado == 6):
		cont1 += 1
	cont +=1
	
cont = cont - 1		
porcentagm = (cont1/cont)*100
print (cont)
print (round(porcentagm, 2))