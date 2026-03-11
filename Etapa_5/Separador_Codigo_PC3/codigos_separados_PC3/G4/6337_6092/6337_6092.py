from numpy import *
vet= array(eval(input("")))
n = int(input(""))
i= 0
s = 0

while i < size(vet):
	if n == vet[i]:
		print(i)
	if n > vet[i]:
		s= s+1
	i= i+1
print(s)		
		
		
	 		