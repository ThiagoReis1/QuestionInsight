nome = input("").lower()
c = 12.011
h = 1.00794
n = 14.00674
o = 15.999
if(nome == "histidina"):
	print(round(6*c+10*h+3*n+2*o,2))
else:
	print(round(c*5+h*10+n+2*o,2))