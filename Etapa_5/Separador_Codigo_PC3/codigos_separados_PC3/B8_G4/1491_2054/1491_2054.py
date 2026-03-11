p=float(input("peso(g): "))

if((0<=p)and(p<=5000)):
	ta=0.03
	tx=20.00
elif((5001<p)and(p<=6000)):
	ta=0.04
	tx=25.00
elif((6001<p)and(p<=7000)):
	ta=0.05
	tx=30.00
elif(p>7000):
	ta=0.06
	tx=35.00
v=p*ta+tx	
val=round(v,2)
print(val)