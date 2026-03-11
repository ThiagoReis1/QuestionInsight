numero= int(input("valor: "))
d1=(numero//1000)
d2=(numero%1000)

r=(d1-d2)**2
if(numero == r):
	mensagem= "atende"
else:
	mensagem= "nao atende"
print(mensagem)
print(numero)