n1 = float(input("digite um valor"))
n2 = float(input("digite um valor"))
n3 = float(input("digite um valor"))
n4 = float(input("digite um valor"))

md = (n1+n2+n3+n4)/4

if(md >= 5.0):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"

print(round(md,2))
print(mensagem)