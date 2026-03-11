from numpy import*
vn= array(eval(input()))
i=0
t=0
while i< size(vn):
	if vn[i]< 2:
		vn[i]= 0 
	elif vn[i]>8:
		vn[i]=10
	i= i+1
print(vn)