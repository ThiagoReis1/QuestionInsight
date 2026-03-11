quant = float(input("quantidade de combustivel: "))
if (quant < 17.5):
	valortotal = quant + 10.5
elif (quant >= 17.5) and (quant <= 35):
	valortotal = quant+ 14
elif (quant >= 35) and (quant <= 50):
	valortotal = quant + 18.6
else: 
	valortotal = quant + 24.5
print(round(valortotal,2))
	
	

