from numpy import *
a = input().split(',')
x = len(a)
i = 0
p = array([0,0,0,0,0])
for i in range(x):
	if(a[i] == 'BE'):
		p[0] = p[0] + 1
	if(a[i] == 'ES'):
		p[1] = p[1] + 1
	if(a[i] == 'FR'):
		p[2] = p[2] + 1
	if(a[i] == 'IT'):
		p[3] = p[3] + 1
	if(a[i] == 'PT'):
		p[4] = p[4] + 1
print(p)