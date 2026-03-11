a = float(input("renda"))
b = float(input("prestacao"))

c = a * (25/100)

if(b > c):
	msg = "Emprestimo nao aprovado"
	
else:
	msg = "Emprestimo aprovado"
	
print(msg)