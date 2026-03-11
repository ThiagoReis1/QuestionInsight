from numpy import*
from numpy.linalg import*
v= array(eval(input('matriz: ')))
i = 0
for i in range (size(v)):
	if v[i] >80:
		x = sum(v)-5
	else:
		x = sum(v)
print(round(x, 2))
	
		
	
	

		
		
		
		