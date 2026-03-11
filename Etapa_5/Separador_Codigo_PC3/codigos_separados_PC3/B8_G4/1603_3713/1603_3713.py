from numpy import*
n =array(eval(input()))
i = 0
l=0
p=0
k=0
while (i<size(n)) and (n[i]!=4):
	if n[i]==1:
		l=l+80
		i = i+1
	elif n[i]==2:
		p = p+40
		i = i+1
	elif n[i]==3:
		k = k+20
		i = i+1	
a = l+k+p
print(a)
		