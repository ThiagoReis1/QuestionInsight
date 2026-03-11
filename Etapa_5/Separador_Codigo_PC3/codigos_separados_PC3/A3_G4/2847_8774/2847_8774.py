from numpy import*

r= array(eval(input()))
z= zeros(size(r), dtype = int)

for i in range(size(r)):
	r[i]= r[i] ** 2
print(r)

		
		