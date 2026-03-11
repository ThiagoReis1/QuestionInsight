ps = float(input())
d = float(input())
c = int(input())

##ctg = (25 * ps)
##ctd = (0.1 * d)

if(c == 1):
	icms = 17
	
elif(c == 2):
	icms = 17.5
	
elif(c == 3):
	icms = 18
	
else:
	icms = 20
	
s1 = ((ps * 25) + (d * 0.1))  
s2 = (1 + (icms / 100))
s3 = s1 * s2

print(round(s3, 2))