from numpy import*

v = array(eval(input("frequencia: ")))
r = 0
for i in range(size(v)):
	if(v[i]<70):
		r = r + 1

i = 0
n = 0
s = zeros(r, dtype=int)
while(size(v)>i):
	if(v[i]<70):
		s[n] = i
		n = n + 1
	i = i + 1

print(r)
print(s)


		
		
	