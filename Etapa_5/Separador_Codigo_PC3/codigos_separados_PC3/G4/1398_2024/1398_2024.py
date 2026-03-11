A=float(input())
if(A<=200):
	B=5000+(A*100)
	print(B)
if(A>200):
	C=A-200
	B=8000+(200*100)+(C*90)
	print(round(B,2))