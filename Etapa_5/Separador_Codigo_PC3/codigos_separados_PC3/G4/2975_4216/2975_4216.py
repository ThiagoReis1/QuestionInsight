qsu = int(input("Quantidade de sucos: "))
qsa = int(input("Quantidade de salgados: "))
vt  = float(input("Valor disponivel: "))

e   =  (qsu*3) + (qsa*3.5)

print(round(e, 2))

if(e<=vt):
	print("Sim")
else:
	print("Nao")