a=float(input("digite um num"))

if(a<=50):
	l=0.10*a
elif(a>50 and a<=100):
	l=0.5*a
elif(a>100 and a<=500):
	l=0.4*a
else:
	l=0.3*a

print(round(l+a,2))
	
	