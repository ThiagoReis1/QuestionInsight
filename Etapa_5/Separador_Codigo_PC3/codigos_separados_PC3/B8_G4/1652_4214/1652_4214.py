from numpy import *

a= array(input("racas:").split(','))

r= zeros(5, dtype=int)

for i in range(size(a)):
	if(a[i] == "B"):
		r[0] = r[0] + 1
	elif(a[i] == "PA"):
		r[1] = r[1] + 1
	elif(a[i] == "PR"):
		r[2] = r[2] + 1
	elif(a[i] == "A"):
		r[3] = r[3] + 1
	elif(a[i] == "I"):
		r[4] = r[4] + 1
	
print(max(r))
print(r)