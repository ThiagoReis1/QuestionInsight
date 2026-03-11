cxes=input()
qnt=int(input())
qnts=int(input())
if (cxes.upper()=="C"):
	vt=(qnt*2)+(qnts*6)
else:
	vt=(qnt*4.5)+(qnts*6)
print(round(vt, 2))