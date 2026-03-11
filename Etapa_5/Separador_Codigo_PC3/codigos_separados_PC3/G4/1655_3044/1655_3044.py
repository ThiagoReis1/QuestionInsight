from numpy import* 
x=input("vetor").split(",")
z=zeros(5,dtype=int)
for i in range(0,size(x)):
	if(x[i]=="AC"):
		z[0]=z[0]+1
	if(x[i]=="AM"):
		z[1]=z[1]+1
	if(x[i]=="PA"):
		z[2]=z[2]+1
	if(x[i]=="RO"):
		z[3]=z[3]+1
	if(x[i]=="RR"):
		z[4]=z[4]+1
print(max(z))
print(z)