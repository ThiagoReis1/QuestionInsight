from numpy import*
v = array(eval(input()))
rep = 0

for i in range(size(v)):
	if(v[i] < 70):
		rep = rep + 1

vr = zeros(rep,dtype=int)
j = 0
for i in range(size(v)):
	if(v[i] <70):
		vr[j] = i
		j = j+1
print(rep)
print(vr)