from numpy import * 

# Entradas

v1 = array(['ARROZ', 'FEIJAO', 'BIS', 'MIOJO', 'FANTA'])
# v2 = array(['1.25', '2.60', '1.80', '0.85', '3.20'])

# Leituras
v3 = array(eval(input("Produto: ")))
v4 = array(eval(input("Quantidade: ")))

# Contador
i = 0
c = 0
x = 0

while (i <= size(v3)):
	if(v3[i] == "ARROZ"):
		c = c + v4[0] * 1.25
	elif(v3[i] == "FEIJAO"):
		c = c + v4[1] * 2.60
	elif(v3[i] == "BIS"):
		c = c + v4[2] * 1.80
	elif(v3[i] == "MIOJO"):
		c = c + v4[3] * 0.85
	else:
		c = c + v4[4] * 3.20
	i = i + 1
print(c)

	
	
	
	
	
	