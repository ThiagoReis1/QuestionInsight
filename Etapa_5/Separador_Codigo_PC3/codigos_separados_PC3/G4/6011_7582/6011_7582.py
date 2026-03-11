vr = float(input("valor da renda "))
vp = float(input("valor da prestracao "))
h = (35/100)
g = h * vr 

if vp > g :
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")