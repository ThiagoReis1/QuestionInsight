q = float(input("Insira a quantidade de combustivel comum: "))

if (q < 17.5):
	b = q + 0.8
elif (17.5 <=q <35):
	b = q + 1.3
elif (35	<=q <50):
	b= q + 2.1
else:
	b = q + 3
print(round(b,1))