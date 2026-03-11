from numpy import*
v1 = array(eval(input("")))
v2 = array(eval(input("")))
n = zeros(size(v1))
k = 0
a = 0
for i in range(size(v1)):
	n[k] = v1[i] + v2[i]
	k += 1
a = 0
for i in n:
	if i >= 12:
		a += 1
print(n)
print(a)

	