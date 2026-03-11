from numpy import*

t = float(input("")) 
#pl = float(input("")) 
#pi = float(input("")) 

if t >= 0 and t <= 100:
	vl= t *80+3000
	
elif t > 100 and t <= 200:
	vl = t *90+4000
	
elif t > 200 and t <= 300:
	vl = t * 100+5000
else:
	
	vl = t*110 + 6000

print(round(vl,2))
