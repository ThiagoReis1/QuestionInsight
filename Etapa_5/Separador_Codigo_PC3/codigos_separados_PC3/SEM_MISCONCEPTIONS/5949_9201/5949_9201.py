a = input("digite a alternativa:").upper()
f= float(input("digite a quant:"))
c= float(input("digite um valor:"))

if a == "B":
	valor1 = f * 3.00 + c * 5.50
	print(valor1)
else:
	valor2 = f * 6.00 + c * 5.50
	print(valor2)