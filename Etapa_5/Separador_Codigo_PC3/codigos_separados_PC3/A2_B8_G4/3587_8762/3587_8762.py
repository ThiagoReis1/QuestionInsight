from numpy import *
vet = array(eval(input("")))
i = 0
t = 100
while i<size(vet):
	if(vet[i]==1):
		t = t*5 
	elif(vet[i]==2):
		t = t*3
	elif(vet[i]==3):
		t = t
	elif(vet[i]==4):
		t = t/2
	i = i+1
	
print(round(t,2))