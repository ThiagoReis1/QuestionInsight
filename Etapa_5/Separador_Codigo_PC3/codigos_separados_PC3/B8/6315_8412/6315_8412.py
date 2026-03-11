carrinho = input("produtos: iogurte(I), massas(M), salgadinhos(S)").upper()
total = 0
i = 0
qtd_i = 0
qtd_m = 0
qtd_s = 0

while i < len(carrinho):
   if carrinho[i] == 'I':
	   total = total + 3.75
	   qtd_i = qtd_i +1
		
   elif carrinho[i] == 'M':
	   total = total + 4.5
	   qtd_m = qtd_m +1
			
   elif carrinho[i] == 'S':
      total = total + 2.9
      qtd_s = qtd_s + 1 
   i = i + 1
print(round(total, 2), qtd_i, qtd_m, qtd_s)