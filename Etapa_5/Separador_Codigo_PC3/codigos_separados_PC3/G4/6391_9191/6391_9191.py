from numpy import*

v=array(eval(input("digite o vetor:")))

for i in range(size(v)):
	if v[i] == 0:
		v[i] = 9
	else:
		v[i] -= 1
			
		
print(v**3)

