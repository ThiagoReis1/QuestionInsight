v= float(input())
nc=int(input())

if(nc==1):
	d= v-(v*0.10)
	vt= d
	print(round(vt,2))

elif(nc==2):
	d= v-(v*0.30)
	vt= d*2
	print(round(vt,2))
	
elif(nc>=3):
	d= v-(v*0.40)
	vt= d*nc
	print(round(vt,2))
	
	