from numpy import*
v = array(eval(input("v: ")))

i = 0
mp = 0

while(i <size(v)):
	mp += (v[i])**2
	i += 1
	
total = (mp/size(v))**(1/2)

print(round(total,2))
	

