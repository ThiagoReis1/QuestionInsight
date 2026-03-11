u = input("informe a unidade de medida: ")

v = float(input("informe o valor da medida: "))

x = u.upper()

if x== "K" :
	lb = (2.20462*v)
	print(round(lb,2))
	
	
else:
	kg = (v/2.20462)
	print(round(kg,2))