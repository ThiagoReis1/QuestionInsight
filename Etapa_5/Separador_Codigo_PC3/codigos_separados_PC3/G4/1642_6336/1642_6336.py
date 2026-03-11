from numpy import*

v = array(eval(input("digite: ")))

cont5 = 0 


for i in range(size(v)):
	if v[i] % 5 == 0:
		cont5 = cont5 + 1 
		
z = zeros(cont5, dtype = int)		
j = 0 

for i in range(size(v)):
	if v[i] % 5 == 0:
		z[j] = i
		j = j + 1 
 	
		
print(cont5)
print(z)
	
		