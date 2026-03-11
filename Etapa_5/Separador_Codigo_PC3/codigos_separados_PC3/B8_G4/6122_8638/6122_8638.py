comb = int(input("quantidade de combustivel: "))

if(comb < 17.5):
	t = comb + 0.8
	print(round(t, 1))
elif(17.5 < comb < 35.0):
	t = comb + 1.3
	print(round(t, 1))
elif(35.0 < comb < 50.0):
	t = comb + 2.1
	print(round(t, 1))
elif(comb > 50):
	t = comb + 3.0
	print(round(t, 1))