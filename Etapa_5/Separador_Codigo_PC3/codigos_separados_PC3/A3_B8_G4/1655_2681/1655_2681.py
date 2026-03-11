from numpy import *

vet1 = input().split(',')

RR = 0
AM = 0
RO = 0
AC = 0
PA = 0
errado = 0
vet2 = zeros(10)
for x in range(len(vet1)):
	if(vet1[x].upper() == 'RR'):
		vet2[x]= x
		RR += 1
	elif(vet1[x].upper() == 'AM'):
		vet2[x] = x
		AM += 1
	elif(vet1[x].upper() == 'RO'):
		vet2[x] =x
		RO += 1
	elif(vet1[x].upper() == 'AC'):
		vet2[x] = x
		AC += 1
	elif(vet1[x].upper() == 'PA'):
		vet2[x] = x
		PA += 1
	else:
		errado=0

if((AM>RR)  and (AM>PA) and(AM>AC) and (AM>RO)):
	print(AM)
elif((RR>AM) and (RR>PA) and (RR>AC) and(RR>RO)):
	print(RR)
elif((PA > AM) and (PA>RR) and(PA>AC) and (PA>RO)):
	print(PA)
elif((AC > AM) and (AC>PA) and(AC>RO) and (AC>RR)):
	p
print(vet2)
print(AM)