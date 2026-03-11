from numpy import*
vet1 = array(eval(input()))
vet2 = array(eval(input()))

i = 0
cons = 0
while i < size(vet1):
	l = (vet2[i]*5)/100
	cons = cons + (vet1[i]*l)
	i = i + 1
print(round(cons,2))
	