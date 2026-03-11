from numpy import*

v = array(eval(input(": ")))

cont = 0

for i in range (size(v)):
	if v[i] >= 70:
		cont = cont + 1
print(cont)

va = zeros(cont, dtype = int)
j = 0

for i in range (size(v)):
	if v[i] >= 70:
		va[j] = i
		j = j + 1
print(va)
		
	