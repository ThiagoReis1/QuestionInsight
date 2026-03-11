# faça seu código aqui!
qtd = int(input("quantidade pedida: "))
q = qtd*20
t = q - (q*(15/100))

if (qtd>3):
	print(round(t,2))
else:
	print(round(q,2))