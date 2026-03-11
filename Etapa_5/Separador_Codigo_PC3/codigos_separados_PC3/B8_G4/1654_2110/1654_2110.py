from numpy import*
c = input().split(',')
am=0
pe=0
mg=0
sp=0
rs=0

for i in c:	
	if(i=="AM"):
		am=am+1
	elif(i=="PE"):
		pe=pe+1
	elif(i=="MG"):
		mg=mg+1
	elif(i=="SP"):
		sp=sp+1
	elif(i=="RS"):
		rs=rs+1

v=array([am,pe,mg,sp,rs])
print(max(v))
print(v)

