ta = str(input("tipo de ataque: "))
qb = int(input("quantidade de baforadas: "))

if(ta == "maritimo"):
	p = "Viserion"
	q = qb*40
else:
	p = "Drogon"
	q = qb*150
print(p)
print(q)