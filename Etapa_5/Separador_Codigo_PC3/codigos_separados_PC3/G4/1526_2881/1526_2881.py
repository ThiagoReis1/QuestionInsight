qim = int(input("Quantidade inicial de mana da bruxa Sosípatra: "))
qg = int(input("Quantidade de mana que ela gasta por dia: "))
qr = int(input("Quantidade de mana que ela recupera durante o sono: "))
dias = 0
mana = qim
while (mana!=0):
	calc = mana-qg+qr
	mana = mana+calc
	dias = dias+1
print (dias)