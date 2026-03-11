from numpy import*
v = input("entre com os estados: ").split(",")
cont = zeros(5,dtype = int)
for i in range(size(v)):
	if(v[i]=="AZ"):
		cont[0]= cont[0]+1
	elif(v[i] == "CA"):
		cont[1]= cont[1]+1
	elif(v[i] == "FL"):
		cont[2]= cont[2]+1
	elif(v[i] == "PA"):
		cont[3]= cont[3]+1
	elif(v[i] == "WI"):
		cont[4]= cont[4]+1
print(max(cont))
print(cont)
