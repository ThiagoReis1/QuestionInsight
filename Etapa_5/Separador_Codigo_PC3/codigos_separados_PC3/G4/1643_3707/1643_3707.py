from numpy import *
a = array(eval(input()))
k = 0
p = ""
for i in range(size(a)):
	if(a[i]>=5):
		k = k+1
print(k)

for q in range(size(a)):
	if(a[q]>=5):
		p = p + str(q) + " "
print("[" + p.strip() + "]")