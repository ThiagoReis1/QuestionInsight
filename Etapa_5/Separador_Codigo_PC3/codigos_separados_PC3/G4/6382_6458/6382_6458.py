from numpy import*

v = array(eval(input("insira seu vetor: ")))

for i in range(size(v)):
	if v[i] == 9:
		v[i] = 0
	else: 
		a = v[i] + 1
		v[i] = a ** 2
		
print(v)
		