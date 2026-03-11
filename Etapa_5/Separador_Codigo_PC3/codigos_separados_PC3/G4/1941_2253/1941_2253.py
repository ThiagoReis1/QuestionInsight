A = input("digite :")

O=15.9994
C=12.011
N=14.00674
H=1.0079

g  = ((C*2)+(H*5)+(N)+(O*2))
s = ((C*3)+(H*7)+(N)+(O*3))


if (A.upper()=="GLICINA"):
	print(round(g,2))
else:
	print(round(s,2))