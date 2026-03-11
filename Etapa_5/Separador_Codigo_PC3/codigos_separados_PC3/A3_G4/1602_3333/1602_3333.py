from numpy import *
tc=array(eval(input("digite o vetor:")))
i=0
r=0
for i in range(size(tc)):
	if ( max(tc)==tc[i] ):
		r=i
print(r)