from numpy import*
m = array(eval(input()))
ms = zeros(size(m), dtype=int)

for i in range(size(m)):
	if (m[i] == 0):
         ms[i] = 9**2
	else:
		ms[i] = (m[i] - 1)**2

print(ms)
	
	
	