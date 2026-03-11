from numpy import*
v = array(eval(input("notas:")))
r = 0

for x in v:
	if(x<5):
		r = r + 1

vz = zeros(r, dtype=int)
j = 0

for i in range(size(v)):
	if(v[i]<5):
		vz[j]=i
		j = j + 1

print(r)
print(vz)