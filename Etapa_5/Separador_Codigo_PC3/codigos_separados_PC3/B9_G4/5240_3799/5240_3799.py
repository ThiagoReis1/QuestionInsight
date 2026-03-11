n=int(input("energia:"))
if(n<100):
	x=0.50
elif(n>=100 and n<250):
	x=0.75
elif(n>=250 and n<500):
	x=1
else:
	x=1.25
y=(n*x)+50
print(round(y,2))