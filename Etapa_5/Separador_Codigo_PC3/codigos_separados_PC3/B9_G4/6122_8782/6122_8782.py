c=float(input(""))
if (c < 17.5):
	ccl= c+0.8
	print(round(ccl,1))
elif (c>=17.5 and c<35.0):
	ccl=c+1.3
	print(round(ccl,1))
elif (c>=35.0 and c<50.0):
	ccl=c+2.1
	print(round(ccl,1))
else:
	ccl=c+3
	print(round(ccl,1))