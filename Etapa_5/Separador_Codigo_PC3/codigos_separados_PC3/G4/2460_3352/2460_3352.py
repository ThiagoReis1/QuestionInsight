pa= float(input("abertura:"))
pf= float(input("fechamento:"))
p=pf-pa
if(p==0):
	print("sem variacao")
elif(p>0):
	print("saldo positivo")
else:
	print("saldo negativo")