Ami = input("digite o aminoacido : ") 
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if (Ami.lower() == leucina) :
	print((6*C) + (13*H) + N + (O*2))
else :
	print((C*6) + (H*15) + (N*2) + (O*2))