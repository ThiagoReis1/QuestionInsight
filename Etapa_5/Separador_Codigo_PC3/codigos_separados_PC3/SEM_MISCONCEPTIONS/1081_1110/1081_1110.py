Nota1 = float(input("string"))
Nota2 = float(input("string"))
Nota3 = float(input("string"))
Nota4 = float(input("string"))

Media = (Nota1 + Nota2 + Nota3 + Nota4) / 4

if(Media >=5 ):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"
print(round(Media, 2))
print(mensagem)
