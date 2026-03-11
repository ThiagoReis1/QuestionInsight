q= float(input("quantidade c. comum: "))

if(q < 17.5)and(q >0):
	cal= q+10.5
elif(q > 17.5)and(q <35.0)and(q>0):
	cal= q+14.0
elif(q > 35.0)and(q < 50.0)and(q>0):
	cal= q+18.6
else:
	cal= q+24.5
print(round(cal,1))