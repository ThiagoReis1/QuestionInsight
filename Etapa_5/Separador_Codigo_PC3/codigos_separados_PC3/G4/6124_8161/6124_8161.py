p = float(input("peso:"))
if(3000<=p<3400):
	x = p*0.8
elif(3400<=p<3900):
	x = p*1.3
elif(3900<=p<4100):
	x = p*2.1
else:
	x = p*3
print(round(x, 1))