c = float(input("Quantidade de combustivel comum? "))
if (c < 17.5):
	q = 1.5
elif (17.5 <= c < 35):
	q = 2.3
elif (35<= c < 50):
	q = 3.3
else: 
	q = 4.7
ct = c + q 
print(round(ct,1))