from numpy import*
v=(input())

v3=v.split(",")

v2=zeros(5, dtype=int)
for x in v3:
	if x=='AC':
		v2[0]=v2[0]+1
	elif x=='AM':
		v2[1]=v2[1]+1
	elif x=='PA':
		v2[2]=v2[2]+1
	elif x=='RO':
		v2[3]=v2[3]+1
	elif x=='RR':
		v2[4]=v2[4]+1
print(max(v2))
print(v2)
