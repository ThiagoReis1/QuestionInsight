from numpy import*
v= input("estado:").split(',')
resto= zeros(5, dtype=int)

for i in range(size(v)):
	if(v[i]=="AZ"):
		resto[0]+=1
	elif(v[i]=="CA"):
		resto[1]+=1
	elif(v[i]=="FL"):
		resto[2]+=1
	elif(v[i]=="PA"):
		resto[3]+=1
	elif(v[i]=="WI"):
		resto[4]+=1

maximo=max(resto)
print(maximo)
print(resto)
