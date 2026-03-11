from numpy import*

v = array(eval(input()))

n1 = 0
n2 = 0
n3 = 0
n4 = 0
i = 0
while i<size(v):
	if v[i]==1:
		n1+=1
	elif v[i]==2:
		n2+=1
	elif v[i]==3:
		n3+=1
	elif v[i]==4:
		n4+=1
	i+=1
v1 = n1*100
v2 = n2*60
v3 = n3*20
v4 = n4*0
t = v1+v2+v3+v4
print(t)