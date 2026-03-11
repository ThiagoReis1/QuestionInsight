sal=float(input("Salario:"))
cod=int(input("Codigo:"))

sal=round(sal,2)

if sal<0 or cod<101 or cod>104:
	print ("Entradas: R$",sal,"e codigo",cod)
	print ("Dados invalidos")
elif cod==101:
	sf=(sal*0.0080)+sal
	sf=round(sf,2)
	print ("Entradas: R$",sal,"e codigo",cod)
	print ("Novo salario: R$",sf)
elif cod==102:
	sf=(sal*0.0065)+sal
	sf=round(sf,2)
	print ("Entradas: R$",sal,"e codigo",cod)
	print ("Novo salario: R$",sf)
elif cod==103:
	sf=(sal*0.0060)+sal
	sf=round(sf,2)
	print ("Entradas: R$",sal,"e codigo",cod)
	print ("Novo salario: R$",sf)
elif cod==104:
	sf=(sal*0.0055)+sal
	sf=round(sf,2)
	print ("Entradas: R$",sal,"e codigo",cod)
	print ("Novo salario: R$",sf)