from numpy import*

v = array(eval(input("vetor de reais: ")))

b= max(v)
a= min(v)

c = 0.75 * a + 0.25 * b
d= 0.25* a + 0.75 *b

x1=0
x2=0

x=([x1,x2])

for i in range(0,size(v),1):
	if (v[i] >= a and v[i]< c):
		x1 = x1 + 1
	elif(v[i]>=d and v[i]<b):
		x2 = x2 + 1

x=array([x1,x2])				
print(x)
