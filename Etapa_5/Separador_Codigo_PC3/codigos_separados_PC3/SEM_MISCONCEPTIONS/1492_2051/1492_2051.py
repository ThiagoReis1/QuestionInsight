
cargahor = float(input("carga horária"))

if (cargahor>=0)and(cargahor<=10):
	pagamento = cargahor*50+500
	print (pagamento)
elif (cargahor>10) and (cargahor<=20):
	pagamento = cargahor*60+600
	print (pagamento)
elif (cargahor>20) and (cargahor<=30):
	pagamento = cargahor*70+700
	print (pagamento)
else:
	pagamento = cargahor*80+800
	print (pagamento)