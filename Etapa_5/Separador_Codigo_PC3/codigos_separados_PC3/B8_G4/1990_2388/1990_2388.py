at = input("aminoacido:")


if  (at.upper() != 'GLUTAMINA') and(at.upper() != 'SERINA') and(at.upper() != 'TREONINA'):
	print("Entrada:", at)
	print("Dado Invalido")
elif  (at.upper() == 'GLUTAMINA'):
	p= (5 * 12.011) + (8*1.00794) + 14.0067 + (4 *15.9994 )
	print(round(p,2))
elif  (at.upper() == 'SERINA') :
	p = (3 * 12.011) + ( 7 *1.00794 ) + 14.0067 + (3 * 15.9994) 
	print(round(p,2))
elif  (at.upper() == 'TREONINA'):
	p= ( 4 * 12.011) + ( 9 *1.00794) + 14.0067 + (3 * 15.9994)
	print(round(p,2))
	
