ataque = input()
rodada = int(input())
valores1 = int(input())
valores2 = int(input())
d = valores1+valores2
if ataque == "constricao":
	dano_total = (d+1)*rodada
else:
	dano_total = valores1*valores2
	
print(dano_total)


	