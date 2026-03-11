#Start!
ask = input("Qual o seu veneno?")
#formulas
feni = ((9*12.011)+(11*1.0079)+(2*15.9994)+(1*32.066))
aspa = ((4*12.011)+(6*1.0079)+(1*14.0067)+(4*15.9994))
tiro = ((9*12.011)+(11*1.0079)+(1*14.0067)+(3*15.9994))
#process
if(ask == "fenilalanina"):
	print(round(183.2507,2))
elif(ask == "tirosina"):
	print(round(181.1908,2))
elif(ask == "aspartato"):
	print(round(132.0957,2))
else:
	print("Entrada:", ask)
	print("Dado Invalido")