from numpy import*

v=array(eval(input("Vetor: ")))
s=0

for i in range(size(v)):
	if v[i]!=88:
		s=s+v[i]
	else:
		s=s/2
print(s)		