from numpy import *

vet = input().upper().split(',')

AC = 0
AM = 0
PA = 0
RO = 0 
RR = 0
for i in range(size(vet)):
	if(vet[i] == AC):
		ac = cm + 1
	elif(vet[i] ==AM):
		am = am + 1 
	elif(vet[i] == PA):
		pa = pa - 1 
	elif(vet[i] == RO):
		ro = ro + 1 
	elif(vet[1] == RR):
		rr = rr + 1 
print(RR)
		

		
	