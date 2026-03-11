from numpy import *
m = array(eval(input("msg: ")))
i = zeros(size(m), dtype=int)
for j in range(0,size(m)):
	if m[j] == 9:
		i[j] = 0
	else:
		i[j] = m[j] + 1
print(i)