from numpy import*

v=array(eval(input("")))
s=zeros(size(v),dtype=float)

c = 0

for i in range(size(v)):
	if v[i]>20:
		s[i]= v[i]
		c+=1
	else:
		s[i]= 0.0
	
if sum(s)==0.0:
	print("0.0")
else:
	media = sum(s)/c
	print(round(media,2))