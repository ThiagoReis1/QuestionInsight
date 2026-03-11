from numpy import*
p = array(input("").split(','))
v = zeros(5,dtype=int)
i= 0
while(i < size(p)):
	if(p[i] == "BE"):
		v[0] = v[0] + 1
	elif(p[i] == "ES"):
		v[1] = v[1] + 1
	elif(p[i] == "FR"):
		v[2] = v[2] + 1
	elif(p[i] == "IT"):
		v[3] = v[3] + 1
	elif(p[i] == "PT"):
		v[4] = v[4] + 1
	i = i + 1
print(max(v))
print(v)