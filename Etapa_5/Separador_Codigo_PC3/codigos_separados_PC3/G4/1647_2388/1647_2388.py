from numpy import*
pc = array(eval(input(": ")))

ap= 0

for i in pc:
	if( i >= 70):
		ap = ap+1

v= zeros(ap, dtype= int)
print(ap)
j=0
for i in range(size(pc)):
	if( pc[i] >= 70):
		v[j] = i
		j =j+1
print(v)