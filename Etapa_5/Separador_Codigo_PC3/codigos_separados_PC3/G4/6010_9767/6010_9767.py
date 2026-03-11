vdr = float ( input ("Valor de renda: "))
vdp = float ( input ("Valor da prestacao: "))


calc = vdr * 0.35 

if ( vdp > calc):
	print ("Emprestimo nao aprovado")
	
else:
	print ("Emprestimo aprovado")