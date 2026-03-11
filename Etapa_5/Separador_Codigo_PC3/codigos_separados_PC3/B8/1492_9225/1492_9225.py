
c = int(input("digite os valores: "))


if c < 10 and c > 0:
	bonifica = 500
	valor = 50
elif c < 20 and c > 10:
	bonifica = 600
	valor = 60
elif c < 30 and c > 20:
	bonifica = 700
	valor = 70
elif c > 30 :
	bonifica = 800
	valor = 80
	
pagamento = c * valor + bonifica


print(round(pagamento,2))
