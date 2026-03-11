cc= input().upper()
e=0
cont=0
while (cc !="S"):
	if cc== "PRETA":
		e= e+1
		cont= cont+1
	else:
		e= e+1	
	cc= input().upper()
pc= ((cont*100)/e)
print(e)
print(round(pc,2))