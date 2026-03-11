from numpy import*
a = array(eval(input("")))
t = 0 

for i in range(size(a)):
	if(a[i]%3 == 0):
		t = t + 1 
x = zeros(t, dtype=int)
k = 0
for i in range(size(a)):
	if(a[i] % 3 == 0):
		x[k] = x[k] + i
		k = k + 1 
print(t)
print(x)
		
		