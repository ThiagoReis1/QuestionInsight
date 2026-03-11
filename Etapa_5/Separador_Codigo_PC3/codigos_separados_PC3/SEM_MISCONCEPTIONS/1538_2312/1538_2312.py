x=float(input("numero x"))
k=int(input("numero k"))
formula=1-x**2+x**4
contagem=1
pot1=2
pot2=4
if k>1:
	while contagem<k:
		pot1=pot1+4
		pot2=pot2+4
		formula=formula-x**pot1+x**pot2
		contagem=contagem+1
print(round(formula,8))