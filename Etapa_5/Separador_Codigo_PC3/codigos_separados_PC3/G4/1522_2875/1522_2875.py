qi= int(input("Quantidade inicial de moedas: "))
dm= int(input("Despesa mensal: "))
qm=int(input("Quantidade M de moedas: "))
qr= int(input("Quantidade R de moedas: "))
meses= 0
soma= (qi+qm)
soma2= (soma - (dm+qr))
while (soma>soma2 ):
	meses= meses+1
print(meses)