from numpy import* 

v = array(eval(input("vetor: ")))
a = 0 

for i in range(size(v)):
	if v[i] != 10:
		a = a + v[i]
	else:
		a = a * 10
		
print(a)
