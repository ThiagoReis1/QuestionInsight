cc = float(input())

if cc<17.5:
	print(round(cc+0.8,4))
elif cc>=17.5 and cc<35:
	print(round(cc+1.3,4))
elif cc>=35 and cc<50:
	print(round(cc+2.1,4))
elif cc>=50:
	print(round(cc+3,4))