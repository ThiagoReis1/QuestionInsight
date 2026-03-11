n1 = float(input("Qual o valor da primeira nota? "))
n2 = float(input("Qual o valor da segunda nota? "))
n3 = float(input("Qual o valor da terceira nota? "))

media = (n1+n2+n3)/3

if(media>=7.0):
	mensagem = ("Aprovado")
else:
	mensagem = ("Reprovado")

print(round(media, 1))
print(mensagem)