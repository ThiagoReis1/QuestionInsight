from numpy import *
a = array(eval(input("")))
s = 0
y = 0
m = 0
for i in range(size(a)):
	if a[i] <= 50:
		s = s + 1	
print(s)
aux = zeros(s, dtype = int)
for i in range(size(a)):
	if a[i] <=50:
		y = i
		aux[m] = y
		m +=1
		
print(aux)



		

	