h = input()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
x = (6*C)+(10*H)+(3*N)+(2*O)
y = (5*C)+(10*H)+N+(2*O)
if(h.lower()=='histidina'):
	print(round(x, 2))
else:
	print(round(y, 2))