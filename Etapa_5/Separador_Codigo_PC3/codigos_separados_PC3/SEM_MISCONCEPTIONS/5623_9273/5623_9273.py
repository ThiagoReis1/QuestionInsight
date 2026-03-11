item = input("item(B ou S)")
quant_b_ou_s = int(input("quant:"))
quant_c = int(input("quantc:"))

if item == "B":
	final = quant_b_ou_s*5.00+quant_c*7.50
else:
	final = quant_b_ou_s*4.0+quant_c*7.50
print(round(final,2))