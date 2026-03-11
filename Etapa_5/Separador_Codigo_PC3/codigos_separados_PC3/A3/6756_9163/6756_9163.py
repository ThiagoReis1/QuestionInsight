# faça seu código aqui!
Dias = int(input("Digite a quantidade de dias reservados: "))
Hospedagem = 175 
total = 0 
	
if Dias < 15: 
	total = Hospedagem * Dias + 20
	
if Dias == 15: 
	total = Hospedagem * Dias + 16
		
	   
if Dias > 15: 
	total = Hospedagem * Dias + 10  
		
print(round(total, 2))		

		
		