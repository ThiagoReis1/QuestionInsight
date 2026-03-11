V1 = float(input("Qual o valor da compra?: "))
V2 = float(input("Qual o valor da compra?: "))
V3 = float(input("Qual o valor da compra?: "))
l = float(input("Qual o limite do cartao?: "))
Vt = V1 + V2 + V3	
if( Vt <= l):
	msg = "Nao ultrapassou"
else:
	msg = "Ultrapassou"
print(round(Vt,2))
print(msg)			  
			  