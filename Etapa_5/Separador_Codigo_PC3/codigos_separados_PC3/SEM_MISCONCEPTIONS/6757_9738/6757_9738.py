# faça seu código aqui!
pizza= int(input())

if pizza < 3:
	total= pizza* 5.00 + 3.00
	print(round(total,2))

elif pizza == 3:
	total= pizza*5.00 + 3.25
	print(round(total,2))
	
else:
	total= pizza*5.00 + 4.50
	print(round(total,2))