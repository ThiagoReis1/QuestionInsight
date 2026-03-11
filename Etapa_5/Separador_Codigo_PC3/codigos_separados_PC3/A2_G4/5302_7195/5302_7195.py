m=float(input("massa inicial:"))
anos=int(input("quantidades de anos:"))

ano=0
m=m
while ano<anos:
	m1=(m/100)*5
	m=m-m1
	ano=ano+1
	print(round(m,2))	
	
	