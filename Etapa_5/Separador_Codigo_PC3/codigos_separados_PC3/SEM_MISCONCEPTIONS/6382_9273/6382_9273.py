from numpy import* 
m = array(eval(input(" :")))
ms = zeros(size(m), dtype=int)

for i in range(size(m)):
	if m[i] == 9:
		ms[i] = 0
	else:
		ms[i] = (m[i] + 1)**2
	
print(ms)
		
	k