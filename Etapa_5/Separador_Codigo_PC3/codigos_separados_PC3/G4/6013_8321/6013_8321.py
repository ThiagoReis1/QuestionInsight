r = float(input("renda: "))
p = float(input("prestacao: "))

if (p >= 0.15*r):
	m = "Emprestimo nao aprovado "
else:
	m ="Emprestimo  aprovado"
print(m)