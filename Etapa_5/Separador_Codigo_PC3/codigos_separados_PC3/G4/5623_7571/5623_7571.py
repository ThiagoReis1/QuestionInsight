fatia= input("salgado ou bolo: ").upper()
qtd= float(input("digite a quantidade: "))
cap= float(input("cappuccinos : "))
B=5*qtd
S=4*qtd
C=7.5*cap
if(fatia=="B"):
	valor= B+C
	print(round(valor,2))
	
if(fatia=="S"):
	valor=S+C
	print(round(valor,2))