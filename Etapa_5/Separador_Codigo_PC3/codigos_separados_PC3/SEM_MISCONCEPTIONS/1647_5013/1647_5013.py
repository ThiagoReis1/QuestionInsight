from numpy import*

p = array(eval(input(": ")))

cont = 0

indice = []

for i in p:
	if i >= 70:
		cont = cont + 1
	
for j in range(size(p)):
	if p[j] >= 70:
		indice.append(j)
		
print(cont)
print(array(indice))
		
	