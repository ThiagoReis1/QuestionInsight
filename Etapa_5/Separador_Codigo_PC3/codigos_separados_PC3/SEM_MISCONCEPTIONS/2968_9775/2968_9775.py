lanche = 5
salgado = 3.50
refri = 4

ls = input()
q_ls = int(input())
q_refri = int(input())

if ls == 'L':
	preco = (lanche * q_ls) + (refri * q_refri)
	print(round(preco, 2))
else :
	preco = (salgado * q_ls) + (refri * q_refri)
	print(round(preco, 2))