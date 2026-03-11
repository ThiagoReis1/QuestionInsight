
produtos = input().upper()
i = 0
total = 0.0
while(i < len(produtos)):
	produto = produtos[i]
	if(produto == 'B'):
		total += 6.8
	elif(produto == 'C'):
		total += 11.75
	elif(produto == 'M'):
		total += 5.9
	i += 1
print(round(total,2))
