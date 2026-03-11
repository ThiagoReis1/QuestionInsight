qi = int(input("Quantidade inicial:"))
dm = int(input("Despesa mensal:"))
qm = int(input("Quantidade M:"))
qr = int(input("Quantidade R:"))
meses = 0
soma = 0

while(qi>0):
	qi = qi - dm + qm - qr
	meses = meses+1
	
print(meses)
	