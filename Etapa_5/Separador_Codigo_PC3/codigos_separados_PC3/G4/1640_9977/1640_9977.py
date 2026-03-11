from numpy import*
a = array(eval(input('Vetor: ')))
b = 0
for i in range(size(a)):
	if a[i] % 2 == 0:
		b= b + 1
c = zeros(b,dtype=int)
d = 0
for i in range(size(a)):
	if a [i] % 2 == 0:
		c[d] = c[d] + i
		d = d +1
		
print(b)
print(c)