ami = input("Aminoacido:")
O=15.999
C=12.011
N=14.00674
H=1.00794

hist = 6*C + 10*H + 3*N + O*2
prol = C*5 + 10*H + N*1 + O*2

if (ami.lower() == 'histidina'):
	print(round(hist,2))
else:
	if (ami.lower() == 'prolina'):
		print(round(prol,2))