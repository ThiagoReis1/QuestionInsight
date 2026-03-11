ps=float(input())

if(ps<=4999.9):
	vl=(ps*0.05)
	print(round(vl,2))
else:
	vll=(ps*0.04)+60
	print(round(vll,2))