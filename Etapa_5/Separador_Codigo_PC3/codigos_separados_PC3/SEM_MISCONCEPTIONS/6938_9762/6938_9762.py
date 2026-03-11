sub_total = float(input())
opcao = input().upper()

if opcao == "D" or opcao == "P":
	desconto = (sub_total) * (11/100)
	total = (sub_total)-desconto
	print(round(total,2))
	
else:
	p = int(input())
	if p == 1:
		print(sub_total)
	else:
		acrescimo = (sub_total) * (6/100)
		total = (sub_total) + acrescimo
		print(round(total,2))
		
			
		
		



	
	
	
	
	
	