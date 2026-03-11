from numpy import *

x = input("Cor dos olhos: ").split(',')

p = 0
c = 0
m = 0
v = 0
a = 0

f=zeros(5,dtype=int)

for i in range (size(x)):
	if x[i] == 'p' or x [i] == 'P':
		p +=1
		f[0] +=1
	elif x[i] == 'c' or x [i] == 'C':
		c += 1
		f[1] +=1
	elif x[i] == 'm' or x [i] == 'M':
		m += 1
		f[2] +=1
	elif x[i] == 'v' or x [i] == 'V':
		v += 1
		f[3]+=1
	elif x[i]=='a'or x[i] == 'A':
		a+= 1
		f[4]+=1


if (p>=c and p>=m and p>=v and p>=a):
	print(p)
elif (c>=p and c>=m and c>=v and c>=a):
	print(c)
elif(m>=c and m>=p and m>=v and m>=a):
	print(m)
elif(v>=p and v>=c and v>=m and v>=a):
	print(v)
elif(a>=p and a>=c and a>=v and a>=m):
	print(a)
print(f)