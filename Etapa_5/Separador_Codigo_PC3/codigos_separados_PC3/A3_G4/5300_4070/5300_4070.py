r=int(input("RPM: "))


cont=0

if r>=50:
	cont=r-r*0.25
	i=0
	while i<=r:
		x=r
		cont=x-cont
		
	print(round(cont,2))
else :
		print(round(r,2))