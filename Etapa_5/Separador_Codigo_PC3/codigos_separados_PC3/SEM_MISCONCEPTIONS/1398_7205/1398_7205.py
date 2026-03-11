a= float(input("tempo: "))
if (a<200):
	b= a*0.05
else:
	d= a-200
	b= (200*0.05)+(d*0.10)
	print(round(b,2))1