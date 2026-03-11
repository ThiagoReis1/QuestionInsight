combustivel = float(input(""))

if combustivel < 17.5:
	total = combustivel + 1.5
elif (combustivel >= 17.5) and (combustivel <=35):
	total = combustivel + 2.3
elif (combustivel >=35) and (combustivel <= 50):
	total = combustivel + 3.3
else:
	total = combustivel + 4.7
print(round(total,1))