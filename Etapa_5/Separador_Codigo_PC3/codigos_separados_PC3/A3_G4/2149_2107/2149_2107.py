from numpy import*
x = array(eval(input))
y = array(eval(input))
r = zeros(3)
a = 0
b = 0
c = 0
for i in range(size(x)):
	a=+1
	r[0]=x[0]+y[0]
	b+=1
	r[1]=x[1]+y[1]
	c+=1
	r[2]=x[2]+y[2]
print(r)
rep=r[1]<12
ap= size(r)-rep
print(ap)
	