com=float(input(""))

if(com>0):
	if(com<17.5):
		tt=com+1.5
	elif(com>=17.5 and com<35):
		tt=com+2.3
	elif(com>=35 and com<50):
		tt=com+3.3
	else:
		tt=com+4.7
print(tt)