v=float(input(""))
if v>0.00 and v<=50.00:
	l=v+v*1.0
elif v>50.01 and v<=100.00:
	l=v+v*0.5
elif v>100.01 and v<=500.00:
	l=v+v*0.4
elif v>500.01:
	l=v+v*0.3
print(round(l,2))