from numpy import * 
var = array(eval(input('')))
cont = 0
cont1 = 0
for i in range(size(var)):
	if(var[i]<=50):
		cont = cont + 1 
s = zeros(cont,dtype = int )

for i in range(size(var)):
	if(var[i]<=50):
		s[cont1] = i
		cont1 = cont1 +1
print(cont)
print(s)
		