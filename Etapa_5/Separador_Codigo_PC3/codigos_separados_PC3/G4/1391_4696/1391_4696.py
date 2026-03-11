cons = float(input("Qual foi o consumo: "))

if(cons<=150):
	i = (cons*0.6)+5
	print(round(i,2))
else:
	ii = (cons*0.75)+16
	print(round(ii,2))