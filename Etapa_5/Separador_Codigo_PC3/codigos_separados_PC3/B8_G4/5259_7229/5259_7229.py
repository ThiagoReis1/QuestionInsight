vm=float(input())
nc=float(input())

if(nc==1):
	v=((vm*-(10/100))+vm)*1
	print(round(v,2))
if(nc==2):
	v=((vm*-(30/100))+vm)*2
	print(round(v,2))
elif(nc>=3):
	v=((vm*-(40/100))+vm)*3
	print(round(v,2))