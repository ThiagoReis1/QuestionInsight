from numpy import*

v = array(eval(input("vetor: ")))
n = 0
j = 0
b = 0
for i in range(size(v)):
	if(v[i]%3 == 0):
		n = n + 1

z = zeros(n,dtype=int)
for i in range(size(v)):
	if(v[i]%3 == 0):
		j = i
		z[b]= j
		b =b +1
		
		 
		
		
		
print(n)
print(z)