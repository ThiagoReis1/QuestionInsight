c=float(input("Salario Atual: "))
d=int(input("Codigo: "))

if((d==101) or (d==102) or (d==103) or (d==104)):
	if(d==101):
    	print("Entradas: R$", c,"e codigo", d)
    	print("Novo salario: R$ ", c+ ((c*8)/1000))
	elif(d==102):
		print("Entradas: R$", c,"e codigo", d)
   	print("Novo salario: R$ ", c+ ((c*65)/10000))
	elif(d==103):
		print("Entradas: R$", c,"e codigo", d)
   	print("Novo salario: R$ ", c+ ((c*6)/1000))
	elif(d==104):
		print("Entradas: R$", c,"e codigo", d)
   	print("Novo salario: R$ ", c+ ((c*55)/10000))
else:
    print("Entradas: R$", c,"e codigo", d)
    print("Dados invalidos")