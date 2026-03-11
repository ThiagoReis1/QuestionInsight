from numpy import*
vn = array(eval(input()))
e=0
j=0
for i in range(size(vn)):
	if vn[i] >= 5:
		e += 1
		

vr = zeros(e, dtype = int)

for i in range(0, size(vn)):
	if vn[i] >= 5:
		
		vr[j] = i
		
		j += 1

print(e)		
print(vr)




