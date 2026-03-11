from numpy import *
vet=array(eval(input()))
i=0
s=0
a_menor_do_baile=vet[i]
while(i<size(vet)):
	if(vet[i]<=a_menor_do_baile):
		a_menor_do_baile=vet[i]
	s=s+vet[i]
	i=i+1
	
print(round((s-a_menor_do_baile)/3,2))
if(((s-a_menor_do_baile)/3)>=5):
	print("APROVOU")
else:
	print("REPROVOU")


