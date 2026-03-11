da = float(input("Valor depositado no Banco A: "))
db = float(input("Valor depositado no Banco B: "))

jA = float(input("Taxa de juros no Banco A: "))

jB = float(input("Taxa de juros no Banco B: "))

DA = da
DB = db
m = 0

if ((da > 0) and (db > 0) and (jA > 0) and (jB > 0) and (DA > DB) and (jA < jB)):
	while (DB <DA):
		DA = DA + (DA * (jA / 100))
		DB = DB + (DB * (jB / 100))
		DA = round(DA, 2)
		DB = round(DB, 2)
		m = m+1
	print(m)
else:
	print("Dados incorretos")
		
		
		
		