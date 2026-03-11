
from numpy import*
m=['CHN','JPN','KOR','MGL','THA']
c=zeros(len(m),dtype=int)
a=(input().split(','))
s=0
for i in range(0,len(a)):
	if a[i]=='CHN':
		c[0]=c[0]+1
	elif a[i]=='JPN':
		c[1]=c[1]+1
	elif a[i]=='KOR':
		c[2]=c[2]+1
	elif a[i]=='MGL':
		c[3]=c[3]+1
	elif a[i]=='THA':
		c[4]=c[4]+1
print(max(c))
print(c)