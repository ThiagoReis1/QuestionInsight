from numpy import*

vc = array(eval(input( )))
i = 0
v = 0
while(i<size(vc)):
	if(vc[i]>=80):
		v = v+(vc[i]-5.0)
	else:
		v = v+vc[i]
	i = i+1
print(round(v, 2))