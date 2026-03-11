from numpy import*
vc = array(eval(input("vc: ")))

i=0

while(i < size(vc)):
	if(vc[i]>80.0):
		vc[i] = vc[i] - (0.15*vc[i])
	i = i + 1
print(round(sum(vc), 2))