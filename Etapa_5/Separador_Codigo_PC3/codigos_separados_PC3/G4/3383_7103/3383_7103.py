uni = input("unidade de medida: ")
valm= float(input("valor da medida: "))

if 	uni == "L":
		kg = valm/2.20462
		print(round(kg,2))
		
else: 
		K = valm
		L = 2.20462*K
		print(round(L,2))