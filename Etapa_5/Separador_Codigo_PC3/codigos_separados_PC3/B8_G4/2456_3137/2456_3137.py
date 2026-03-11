vm= float(input("vm: "))
nc= int(input("nc: "))
if (nc==1):
	vt= (m*0.10)
	print(vt)
elif (nc ==2):
	vt= vm*0.30 * nc
	print(vt)
elif nc >= 3 :
	vt= vm*0.40* nc
	print(vt)
