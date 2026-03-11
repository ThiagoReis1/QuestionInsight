deposit = float(input("Deposito inicial: "))
time = int(input("Tempo de aplicacaoo em meses: "))


count_time = 0
interest = 0.01
final_amount = deposit

while count_time < time:
	final_amount += final_amount * interest
	count_time += 1
	print(round(final_amount, 2))
	
	