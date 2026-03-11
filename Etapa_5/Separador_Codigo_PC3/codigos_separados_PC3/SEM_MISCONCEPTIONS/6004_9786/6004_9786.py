quantidade_tomates = int(input('Insira a quantidade de tomates:'))

if quantidade_tomates < 4:
	total = quantidade_tomates * 0.75
else:
	total = quantidade_tomates * 0.55
								 
print(round(total,2))

