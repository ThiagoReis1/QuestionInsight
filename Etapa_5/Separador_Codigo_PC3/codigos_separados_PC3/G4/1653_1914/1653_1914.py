from numpy import*
v = input("")
v = v.replace(",","")
cont = zeros(5,dtype=int)
for i in range(0,len(v),2):
	if(v[i]+v[i+1] == "AR"):
		cont[0] = cont[0] + 1
	elif(v[i]+v[i+1] == "BR"):
		cont[1] = cont[1] + 1
	elif(v[i]+v[i+1] == "CL"):
		cont[2] = cont[2] + 1
	elif(v[i]+v[i+1] == "CO"):
		cont[3] = cont[3] + 1
	else:
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)
