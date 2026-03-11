from numpy import*
v = array(eval(input("Diga bebe: ")))

i = 0
desc = 15/100

while(i < size(v)):
	if(v[i] > 80):
		v[i] = v[i] - (v[i] * desc) 
	else:
		v[i] = v[i]
	i = i + 1

print(round(sum(v),2))