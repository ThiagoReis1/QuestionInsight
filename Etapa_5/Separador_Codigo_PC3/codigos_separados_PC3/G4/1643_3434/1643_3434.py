from numpy import*
v = array(eval(input("vetor: ")))
a = 0
for x in v:
	if (x >= 5):
		a = a + 1
print (a)
r = zeros(a,dtype=int)
i = 0
j = 0
while(i < size(v)):
	if(v[i]>=5):
		r[j]=i
		j = j + 1
		i = i + 1
	else:
		i = i + 1
print(r)
	