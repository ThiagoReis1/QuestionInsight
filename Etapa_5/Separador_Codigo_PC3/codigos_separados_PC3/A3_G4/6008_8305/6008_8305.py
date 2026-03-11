vr = float(input(" qual o valor da renda?: "))
vp = float(input(" qual o valor da prestacao?: "))
total = 0

m = vr * (20/100)
if vp > m:
	total = "Emprestimo nao aprovado"
else:
	total = "Emprestimo aprovado"
	
print(total)