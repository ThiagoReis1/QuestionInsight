#usuario informe a notas.
nota1= float(input("Digite a nota da prova primeira prova: "))
nota2= float(input("Digite a nota da prova segunda prova: "))
nota3= float(input("Digite a nota da prova terceira prova: "))
md= round(((nota1+nota2+nota3)/3),1)
if md>=5:
	print(md)
	print("Aprovado")
else:
	print(md)
	print("Reprovado")