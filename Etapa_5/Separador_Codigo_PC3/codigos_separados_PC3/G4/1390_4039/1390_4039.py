m=int(input())
if(m<=100):
	m1=m*1.20
	print(round(m1, 2))
else:
	t1=m-100
	t2=100*1.40
	t3=t1*1.40
	t=t2+t3+25.0
	print(round(t, 2))