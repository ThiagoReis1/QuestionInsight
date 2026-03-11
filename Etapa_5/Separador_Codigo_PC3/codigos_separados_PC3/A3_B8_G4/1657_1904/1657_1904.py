from numpy import*
v = str(input("vetor:")) .split(",")
az=0
ca=0
fl=0
pa=0
wi=0
maior=0
v1=[]
for i in v:
	if i=="AZ":
		az=az+1
	elif i=="CA":
		ca=ca+1
	elif i=="FL":
		fl=fl+1
	elif i=="PA":
		pa=pa+1
	elif i=="WI":
		wi=wi+1
r=0
v1=array([az,ca,fl,pa,wi])
print(max(v1))
print(v1)

	