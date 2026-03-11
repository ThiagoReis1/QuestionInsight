opcao=input("t ou s: ")
qtd=int(input("quantdade de t ou s: "))
a=int(input("qts de acai: "))
tp = (qtd*4.50) + (a*12)
sl = (qtd*5) + (a*12)

if(opcao.upper()=="T"):
	print(round(tp,2))
else:
	print(round(sl,2))