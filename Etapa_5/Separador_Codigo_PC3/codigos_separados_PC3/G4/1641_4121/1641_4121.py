from numpy import*
v = array(eval(input()))

nt=0

for i in range(size(v)):
	if(v[i] % 3 == 0):
		nt = nt + 1
		
c = zeros(nt,dtype=int)
d=0
for e in range(size(v)):
	if(v[e]%3==0):
		c[d]=e
		d = d + 1
print(nt)
print(d)

			

			