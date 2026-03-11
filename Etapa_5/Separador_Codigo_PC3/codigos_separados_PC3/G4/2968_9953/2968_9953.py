pdd=input()
q=int(input())
qr=int(input())
if pdd.upper()=="L":
	pf=q*5+qr*4
	print(round(pf,2))
if pdd.upper()=="S":
	pf=q*3.5+qr*4
	print(round(pf,2))
