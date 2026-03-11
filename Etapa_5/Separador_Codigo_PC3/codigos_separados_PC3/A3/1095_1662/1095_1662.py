
Numero	=	int(input("Qual	o	numero:	"))
Formula	=	(Numero//10000	+	Numero%10000)**2

if	(Numero ==	Formula):
	mensagem = "x atenda a propriedade"
else:
	print(Formula)

