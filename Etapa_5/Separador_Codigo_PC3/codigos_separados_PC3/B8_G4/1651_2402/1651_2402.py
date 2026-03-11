from numpy import*
v = input().split(',')
cont = zeros(6,dtype=int)

for i in range(size(v)):
	if(v[i]== "MC"):
		cont[0]= cont[0] +1
	elif(v[i]== "C"):
		cont[1]=cont[1]+1
	elif(v[i]=="CM"):
		cont[2]= cont[2]+1
	elif(v[i]== "EM"):
		cont[3]=cont[3]+1
	elif(v[i]=="E"):
		cont[4]= cont[4]+1
	elif(v[i]=="ME"):
		cont[5]= cont[5]+1
		
print(max(cont))
print(cont)