x=input("libras ou quilogramas ")
m=float(input("medida "))

if(x=="L"):
	total= m/2.20462
else:
	total= 2.20462*m

print(round(total,2))