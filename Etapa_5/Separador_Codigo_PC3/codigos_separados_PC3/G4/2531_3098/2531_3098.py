qt=float(input("dinheiro ganho: "))
qtr=float(input("dinheiro de saque: "))
pc=float(input("juros ao mes: "))
meses=0
b=qt+qt*0.1
while(qt<b and qt>0):
	qt = qt + (pc/100) * qt - qtr 
	qt=round(qt,2)
	meses = meses + 1
if(qtr>0 and qt>0 and pc>0):
	print(meses)
else:
	print("Dados incorretos")
		
		
	