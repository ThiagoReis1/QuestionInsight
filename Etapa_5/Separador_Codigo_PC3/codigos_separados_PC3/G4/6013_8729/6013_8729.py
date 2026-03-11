vr = float(input("valor da renda: "))
vp = float(input("valor da prestacao: "))
 
if(vp>=vr*(15/100)):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")