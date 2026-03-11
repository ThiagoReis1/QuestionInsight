from numpy import*
co = input("digite as cores:").split(',')
v = zeros(5,dtype=int)
for i in range(size(co)) :
	if(co[i]=="P"):
		v[0] = v[0] + 1
	elif(co[i]=="C"):
		v [1]= v[1] + 1
	elif(co[i]=="M"):
		v[2] = v[2] + 1
	elif(co[i]=="V"):
		v[3] = v[3] + 1
	elif(co[i]=="A"):
		v[4] = v[4] + 1
print(max(v))
print(v)