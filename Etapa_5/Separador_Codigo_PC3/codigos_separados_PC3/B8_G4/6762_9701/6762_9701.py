# faça seu código aqui!
age = int(input("Qual sua idade? "))
tax = 20
if age < 12:
	tax = tax + 1.25
elif age == 12:
	tax = tax + 2.25
elif age > 12:
	tax = tax + 3.25
print(round(tax, 2))