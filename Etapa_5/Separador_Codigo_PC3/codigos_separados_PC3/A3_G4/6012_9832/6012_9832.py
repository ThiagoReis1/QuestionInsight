r = input("Renda do seu Paulo: ")
p = input("Prestacao mensal: ")

try :
	r = float(r)
	p = float(p)
	
except ValueError :
	print("Digitai numeros mano...")
	
else :
	if ( r < 0 or p < 0 ) :
		print("Digitava valores positivos bro...")
		
	else :
		d = 0
		d = r * 0.25
		
		if ( p > d ) :
			print("Emprestimo nao aprovado")
			
		else :
			print("Emprestimo aprovado")