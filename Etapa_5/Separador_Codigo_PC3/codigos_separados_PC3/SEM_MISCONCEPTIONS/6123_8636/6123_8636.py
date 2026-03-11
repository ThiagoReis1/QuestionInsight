comum = float(input("digite a quantidade de combustivel comum: "))

if comum < 17.5:
	total = comum + 0.8
	print(round(total, 1))
elif comum > 17.5 and comum < 35.0:
	total = comum + 1.3
	print(round(total, 1))
elif comum > 35.0 and comum < 50.0:
	total = comum + 2.1
	print(round(total, 1))
else:
	comum >= 50.0
	total = comum + 3.0
	print(round(total, 1))
	