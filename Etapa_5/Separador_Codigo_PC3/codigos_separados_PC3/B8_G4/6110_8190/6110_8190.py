x= float(input("q "))

if(x<17.5):
	r=x+10.5
elif(x>17.5 and x<35):
	r=x+14
elif(x>35 and x<50):
	r=x+18.6
elif(x>=50):
	r=x+24.5
	
print(round(r,1))