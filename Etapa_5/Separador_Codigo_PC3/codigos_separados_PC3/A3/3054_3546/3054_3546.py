ch = float(input("Carga horaria: "))
pagamento = 0
if( ch <= 10):
	pagamento = ch*50 + 500
elif(ch <= 20):
	pagamento = ch*60 + 600
elif(ch <= 30):
	pagamento = ch*70 + 700
else:
	pagamento = ch*80 + 800

print(round(pagamento, 2))