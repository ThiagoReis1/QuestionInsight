from numpy import*

a = array(eval(input("notas:")))

c = 0


for i in range(size(a)):
	if(a[i] >= 5.0):
		c = c + 1

cont = zeros(c,dtype=int)		
j = 0
	
for i in range(size(a)):
	if(a[i] >= 5.0):
		cont[j] = i
		j = j + 1
		
print(c)
print(cont)
		
		
	
	
	
	
	
