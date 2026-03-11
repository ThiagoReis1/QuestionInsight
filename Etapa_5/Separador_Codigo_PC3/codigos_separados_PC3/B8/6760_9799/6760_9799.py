lavagem = int(input())
custo = 30 

if lavagem < 10:
	  taxa = 3.25
elif lavagem == 10:
	  taxa = 4.50
elif lavagem > 10:
	  taxa = 6.00

total = custo + taxa

print(round(total, 2))