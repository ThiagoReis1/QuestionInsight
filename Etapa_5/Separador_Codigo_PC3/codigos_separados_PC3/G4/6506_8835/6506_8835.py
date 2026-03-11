# faça seu código aqui!
pr = int(input("Pratos:"))
qa = input("s ou n:")
if (qa) == "s":
	cal = (pr*40)*0.95
else:
	cal = pr*40
print(round(cal,2))
	