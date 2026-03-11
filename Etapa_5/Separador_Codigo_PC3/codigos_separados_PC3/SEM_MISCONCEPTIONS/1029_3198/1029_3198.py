minuto = 0.28
fixo = 23.00
consm = float(input())

total = (fixo) + (minuto * consm)
	
percentual = (total * 31/100)

icms = total + (percentual)

total2 = (icms)
		  
print(round(total2,2))



