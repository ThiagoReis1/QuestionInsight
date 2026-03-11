from numpy import*
tp = input("dig cor da pele: ").split(",")
v = zeros(6,dtype=int)
for i in range(0,size(tp)):
	if(tp[i]=="MC"):
		v[0] = v[0]+1
	elif(tp[i]=="C"):
		v[1] = v[1]+1
	elif(tp[i]=="CM"):
		v[2] = v[2]+1
	elif(tp[i]=="EM"):
		v[3] = v[3]+1
	elif(tp[i]=="E"):
		v[4] = v[4]+1
	elif(tp[i]=="ME"):
		v[5] = v[5]+1
print(max(v))
print(v)
	
	