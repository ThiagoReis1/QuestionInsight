from numpy import*
x = (input(": "))
e = x.split(',')

b = 0
pa = 0
pr = 0
a = 0
i = 0

q = zeros(5,dtype=int)

for t in e:
	if (t.upper()=="B"):
		b = b+1
		q[0]=b
	if (t.upper()=="PA"):
		pa = pa+1
		q[1]=pa
	if (t.upper()=="PR"):
		pr = pr+1
		q[2]=pr
	if (t.upper()=="A"):
		a = a+1
		q[3]=a
	if (t.upper()=="I"):
		i=i+1
		q[4]=i

l = q[0]
for i in q:
	if(i>l):
		l = i
print(l)
print(q)