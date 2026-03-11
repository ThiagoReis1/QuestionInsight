vt= float(input())
c= input().upper()
if (c=="C"):
	vp= int(input())
	if (vp == 1):
		print(vt)
	else:
		a= (vt*0.08)
		at= vt+a
		print(round(at,2))
elif (c== "D") or (c=="P"):
	d= (vt*0.13)
	dt= vt-d
	print(round(dt,2))
