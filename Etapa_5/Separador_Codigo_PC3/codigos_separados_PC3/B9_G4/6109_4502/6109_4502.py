n = float(input())
if n<17.5:
	print(round(n+1.5,1))
elif n>=17.5 and n<35:
	print(round(n+2.3,1))
elif n>=35 and n<50:
	print(round(n+3.3,1))
else:
	print(round(n+4.7,1))