Nm = (float(input("Qual o número de mols?: ")))
V = (float(input("Qual o volume?: ")))
T = (float(input("Qual a temperatura?: ")))

kelvin = T + 273.1
p = (Nm * 0.082057 * kelvin ) / (V)
print(p)			  
			  
			  
		