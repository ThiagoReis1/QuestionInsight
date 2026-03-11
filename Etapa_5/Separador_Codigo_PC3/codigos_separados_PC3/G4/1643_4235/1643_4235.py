from numpy import *
nota = array(eval(input("notas: ")))
ap = 0
for i in range(size(nota)):
	if(nota[i]>=5):
		ap= ap+1
print(ap)
v = zeros(ap,dtype=int)
pos = 0
for i in range(size(nota)):
	if(nota[i]>=5):
		v[pos] = i
		pos = pos+1
print(v)





		
	
		