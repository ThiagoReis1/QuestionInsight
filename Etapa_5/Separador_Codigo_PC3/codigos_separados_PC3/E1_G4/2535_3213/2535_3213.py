da = float(input("DA: "))
db = float(input("DB: "))
ja = float(input("TJA: "))
jb = float(input("TJB: "))

cont = 0
somaa = da
somab = db

if (da > 0 and db > 0 and ja > 0 and jb > 0 and da > db and ja < jb):
	while ( somaa > somab):
		ta = (somaa * ja)/100
		somaa = somaa + ta
		tb = (somab * jb)/100
		somab = somab + tb
		cont = cont + 1
		somaa = round(somaa, 2) 
		somab = round(somab, 2)
	print(cont)
else:
	print("Dados incorretos")
	
#print(cont)
