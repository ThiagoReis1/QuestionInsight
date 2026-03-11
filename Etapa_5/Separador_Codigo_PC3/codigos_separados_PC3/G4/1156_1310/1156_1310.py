n=float(input("Numero de cancerosas: "))
p=float(input("Percentual: "))
c=float(input("novas celelulas: "))
e=n
q=15
t=500000
while t>e:
	e=(e - e*p) + c
	q=15+q
print(q/15)