from numpy import *

vet = array(eval(input("aneis acertados: ")))

i = 0
s = 0

while (i<size(vet)):
	if (vet[i] == 1):
		s = s + 100
		
	elif (vet[i] == 2):
		s = s + 60
		
	elif (vet[i] == 3):
		s = s + 20
		
	elif (vet[i] == 4):
		s = s + 0
		
	i = i + 1
	
print (s)
		
	