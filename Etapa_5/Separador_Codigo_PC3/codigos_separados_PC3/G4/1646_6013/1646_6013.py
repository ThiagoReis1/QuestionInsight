from numpy import*

v = array(eval(input("valores")))
aux = zeros(size(v),dtype=int)
c = 0

for i in range(size(v)):
	
	if (v[i]<=50):
		aux[c]=i
		c+=1
print(c)
print(aux[:c])

