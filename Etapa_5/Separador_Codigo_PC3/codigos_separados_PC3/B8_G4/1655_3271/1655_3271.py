from numpy import*

vet=input("informe: ").split(',')
res=zeros(5,dtype=int)

for x in vet:
	if(x=="AC"):
		res[0]+=1
	elif(x=="AM"):
		res[1]+=1
	elif(x=="PA"):
		res[2]+=1
	elif(x=="RO"):
		res[3]+=1
	elif(x=="RR"):
		res[4]+=1

print(max(res))
print(res)