qtde = int(input(" qtde combustivel comum")) 
total = 0

if qtde < 17.5 :
	total= qtde + 1.5
	print(total)
elif qtde >= 17.5 and qtde < 35:  
	total= qtde + 2.3
	print(total)
elif qtde >= 35 and qtde <50:
   total= qtde + 3.3
elif qtde >= 50:
	total= qtde + 4.7
	print(total)