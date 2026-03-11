A = input("aminoacido:")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.00794
a = (C*6)+(H*15)+(N*4)+(O*2)
t = (C*9)+(H*11)+(N*1)+(O*3)

if(A.upper() == "ARGININA"):
	print(round(a,2))
else:
	print(round(t,2))
	
	
