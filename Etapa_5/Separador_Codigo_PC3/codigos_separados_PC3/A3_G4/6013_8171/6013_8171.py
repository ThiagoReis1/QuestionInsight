rend=float(input(""))
val=float(input(""))
out="Emprestimo aprovado"

if val>0.15*rend:
	out="Emprestimo nao aprovado"
	
print(out)
