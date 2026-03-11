from numpy import*
t = array(eval(input()))
x = 0
for i in range(0,size(t)):
	if t[i]%3==0:
		x+=1
print(x)
a = zeros(x,dtype=int)
b=0
for i in range(0,size(t)):
	if t[i]%3==0:
		a[b]=i
		b+=1
print(a)