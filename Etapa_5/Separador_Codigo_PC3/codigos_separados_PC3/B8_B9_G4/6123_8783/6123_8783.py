c=float(input())
if c>0:
	if c<17.5:
		r=c+0.8
	elif c>=17.5 and c<35:
		r=c+1.3
	elif c>=35 and c<50:
		r=c+2.1
	elif c>=50:
		r=c+3.0
print(round(r,1))