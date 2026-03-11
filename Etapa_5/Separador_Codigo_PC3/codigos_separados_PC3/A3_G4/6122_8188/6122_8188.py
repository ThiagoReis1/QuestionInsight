c=int(input("quantidade combustivel "))

if c<17.5:
	x=(c+0.8)
	print(x)
	
elif (17.5<=c) and (c<35):
	y=c+1.3
	print(c+1.3)
	
elif (35<=c) and (c<50):
	w=c+2.1
	print(w)
	
else:
	print(c+3)