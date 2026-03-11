from numpy import*

r= array(eval(input("numero")))
z = zeros(size(r),dtype=int)
c=0

for c in range(size(r)):
	z[c]= r[c]*2

print(z)
	
	
