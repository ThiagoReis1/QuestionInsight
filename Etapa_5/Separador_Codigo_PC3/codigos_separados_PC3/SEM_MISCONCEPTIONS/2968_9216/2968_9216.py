ls = input ("Digite S para salgado e L para lanche: ")
quanti_ls = float (input ("Digite a quantidade desse produto: "))
quanti_ref = float (input ("Digite a quantidade de refrigerantes: "))

ref = quanti_ref * 4

if (ls.upper() == "S"):
	s = quanti_ls * 3.50
	total = s + ref
	print (round (total,2))
if (ls.upper() == "L"):
	l = quanti_ls * 5
	total = l + ref
	print (round(total,2))
	