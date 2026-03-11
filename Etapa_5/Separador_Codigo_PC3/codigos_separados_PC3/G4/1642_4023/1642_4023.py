from numpy import *

x = array(eval(input("Digite o vetor: ")))

cont = 0
j = 0

#############################################

for i in range(size(x)):
	if (x[i] % 5 == 0):
		cont = cont + 1
		
##############################################

s = zeros(cont,dtype=int)
for i in range(size(x)):
	if (x[i] % 5 == 0):
		s[j] = i
		j = j + 1
###############################################

print(cont)
print(s)	
	
	
	
	