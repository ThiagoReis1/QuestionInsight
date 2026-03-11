p=float(input("Valor do produto: "))
c=float(input("Codigo da regiao: "))

if c==1:
	v=(p-(p*0.4))+p*(p*0.1/100)
	print(round(v,2))