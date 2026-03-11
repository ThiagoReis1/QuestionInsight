su = int(input("Quantidade de suco: "))
sa = int(input("Quantidade de salgado: "))
v = float(input("Valor disponivel: "))
t = (su*3)+(sa*(3.5))

if (t <= v):
	print(round(t, 2))
	print("Sim")
else:
	print(round(t, 2))
	print("Nao")