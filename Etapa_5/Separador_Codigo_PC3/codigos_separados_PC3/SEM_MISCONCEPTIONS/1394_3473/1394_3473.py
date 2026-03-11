hr = float(input())

if hr <= 20:
	pagamento = hr*50.00
else:
	pagamento = 1000 + (hr-20)*70

print(round(pagamento,2))