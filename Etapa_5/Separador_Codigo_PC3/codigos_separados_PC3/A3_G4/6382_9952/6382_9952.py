from numpy import*
a = array(eval(input()))
b = zeros(size(a),dtype=int)
for i in range(size(a)):
	if a[i] == 9:
		a[i] = 0
	else:
		a[i] = (a[i] + 1)**2
print(a)
			 