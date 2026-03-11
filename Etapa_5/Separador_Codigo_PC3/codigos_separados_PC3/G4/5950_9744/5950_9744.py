oq = input()
qtd = int(input())
qtdc = int(input())
if(oq=="T"):
	tot = 6*qtd+qtdc*4.5
	print(round(tot, 2))
else:
	tot = 5*qtd+qtdc*4.5
	print(round(tot, 2))