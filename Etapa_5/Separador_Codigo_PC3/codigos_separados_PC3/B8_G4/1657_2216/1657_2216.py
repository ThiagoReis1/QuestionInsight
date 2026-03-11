from numpy import * 
p= input("hf").upper().split(',')
s=zeros(5,dtype=int)
az=0
ca=0
fl=0
pa=0
wi=0
for i in range(len(p)):
	if(p[i]=="AZ"):
		az=az+1
		s[0]=az
	elif(p[i]=="CA"):
		ca=ca+1
		s[1]=ca
	elif(p[i]=="FL"):
		fl=fl+1
		s[2]=fl
	elif(p[i]=="PA"):
		pa=pa+1
		s[3]=pa
	elif(p[i]=="WI"):
		wi=wi+1
		s[4]=wi
print(max(s))
print(s)