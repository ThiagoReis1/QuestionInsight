qtde = float(input())

if qtde < 17.5:
	t = qtde + 0.8
	print(round(t,1))
	
elif qtde >= 17.5  and qtde < 35:
	t = qtde + 1.3
	print(round(t,1))
elif qtde <= 35 and qtde < 50:
	t = qtde + 2.1
	print(round(t,1))
elif qtde >= 50:
	t = qtde + 3
	print(round(t,1))
