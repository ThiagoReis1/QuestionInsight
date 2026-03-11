comum = float(input("Informe a quantidade de combustivel comum disponivel: "))

if(comum < 17.5):
	comb = comum + 10.5
elif(comum >= 17.5 and comum < 35.0):
	comb = comum + 14.0
elif(comum >= 35.0 and comum < 50.0):
	comb = comum + 18.6
elif (comum > 50.0):
	comb = comum + 24.5
	
print(round(comb,2))