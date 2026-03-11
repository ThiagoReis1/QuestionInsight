qp=int(input())
s=input()
if (s.upper()=="S"):
	vt=((qp*40)-((qp*40)*(5/100)))
else:
	vt=(qp*40)
print(round(vt, 2))