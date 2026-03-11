ht = float(input("horas trabalhadas: "))
u = ht*50
if		ht<=20:
		pag = u
		print(round(pag,2))
		
else:
		hextra = ht - 20
		rextra= hextra *70
		r = 20*50
		pag = r + rextra
		print(round(pag,2))