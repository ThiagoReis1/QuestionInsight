from numpy import *

vet1 = input().split(',')

B= 0
PA = 0
PR = 0
A = 0
I = 0
errado = 0
vet2 = zeros(5,dtype=int)
for x in range(len(vet1)):
	if(vet1[x].upper() == 'B'):
		B += 1
	elif(vet1[x].upper() == 'PA'):
		PA += 1
	elif(vet1[x].upper() == 'PR'):
		PR += 1
	elif(vet1[x].upper() == 'A'):
		A += 1
	elif(vet1[x].upper() == 'I'):
		I += 1
	else:
		errado=0

vet2[0]=B
vet2[1]=PA
vet2[2]= PR


if((B>PA)  and (B>PR) and(B>A) and (B>I)):
	print(B)
elif((PA>B) and (PA>PR) and (PA>A) and(PA>I)):
	print(PA)
elif((PR > B) and (PR>PA) and(PR>A) and (PR>I)):
	print(PR)
elif((I > B) and (I>PR) and(I>PA) and (I>A)):
	print(I)
else:
	print(A)
print(vet2)