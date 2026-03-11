vt= float(input())
if vt <= 300:
	tt= vt * (10/100)
	tv= tt + vt
else: 
	ts= vt * (6/100)
	tv= ts + vt
	
print(round(tv, 2))	