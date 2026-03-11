from numpy import*
a = array(eval(input("")))
x = zeros(size(a), dtype=int)
k = 0
for i in range(size(a)):
	if (a[i] != 1):
		k = k + 1
		x[i] = x[i] + a[i]
	if (a[i] == 1):
		x[k] = x[k] + a[i]
print(x)
	


		
