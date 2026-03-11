t=float(input('tempo: '))
if t>0 and t<=200:
	c=(5000+100*t)
if t>200:
	c=8000+(100*200)+ 90*(t-200)
print(round(c,2))