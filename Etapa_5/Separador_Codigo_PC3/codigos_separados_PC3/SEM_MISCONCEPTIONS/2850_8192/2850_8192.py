from numpy import*

v = array(eval(input("digite o vetor:")))

total = 0

for i in range(size(v)):
	total = total + v[i]
	if ( total >= 55):
		total = 0
print(total)
	
	
		

	




