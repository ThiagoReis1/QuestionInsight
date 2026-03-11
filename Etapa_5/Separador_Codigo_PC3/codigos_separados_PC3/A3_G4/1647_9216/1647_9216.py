from numpy import *

num = array(eval(input("Digite: ")))
count = 0
b = 0
x = 0
for i in range(size(num)):
	if (num[i] >= 70):
		count = count + 1
print(count)

a = count
d = zeros(a,dtype=int)

for i in range(size(num)):
	if (num[i] >= 70):
		d[x] = i
		x = x + 1
		
print(d)