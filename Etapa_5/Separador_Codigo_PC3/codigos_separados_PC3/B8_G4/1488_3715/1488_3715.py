m=float(input())

if((m>0) and (m<=100)):
	v=m*1.20+1.0
	print(round(v, 2))
elif((m>100) and (m<=200)):
	v=m*1.30+10.0
	print(round(v, 2))
elif((m>200) and (m<=300)):
	v=m*1.40+20.0
	print(round(v, 2))
elif(m>300):
	v=m*1.50+25
	print(round(v, 2))
	