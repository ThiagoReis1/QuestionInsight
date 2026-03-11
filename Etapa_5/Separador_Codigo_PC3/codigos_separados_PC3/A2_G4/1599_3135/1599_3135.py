from numpy import*
V=array(eval(input("Insira os valores:")))

i=0
s=0

while(i<size(V)):
	if(V[i]>80.0):
		s=s+1
		i=i+1
	else:
		s = s
		i = i + 1
ss= s *0.15
z=sum(V) - ss

print(round(z,2))
		