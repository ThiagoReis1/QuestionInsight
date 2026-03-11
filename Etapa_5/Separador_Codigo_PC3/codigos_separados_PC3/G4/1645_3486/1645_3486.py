from numpy import*
v = array(eval(input('digite um valor:')))
n = 0
b = 0
a = zeros(n, dtype=int)
for i in range(size(v)):
	if(v[i] >= 2000):
		n = n + 1
print(n)
for i in range(size(v)):
	if(v[i] >= 2000):
		a[b] = i 
		b = b + 1
		print(b)

