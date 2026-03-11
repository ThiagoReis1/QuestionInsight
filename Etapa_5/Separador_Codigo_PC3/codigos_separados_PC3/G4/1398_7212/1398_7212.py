t=float(input())

if(t<=200):
	p= 5000+(100*t)
	print(round(p,2))
else:
	p= 8000+(100*200+(t-200)*90)
	print(round(p,2))