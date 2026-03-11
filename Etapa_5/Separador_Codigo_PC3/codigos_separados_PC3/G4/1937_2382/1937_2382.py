amino=input().upper()
O=15.9994
C=12.011
N=14.00674
H=1.00794

if(amino=="ALANINA"):
	print(round(3*C+7*H+N+2*O,2))
if(amino=="VALINA"):
	print(round(5*C+11*H+N+2*O,2))