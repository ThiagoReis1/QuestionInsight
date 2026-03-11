from numpy import*

estado = input("estado:").split(',')

i = 0
contaz = 0
contca = 0
contfl = 0
contpa = 0
contwi = 0
conti = 0

while (i < len(estado)):
	if(estado[i] == "AZ"):
		contaz = contaz + 1
		i = i + 1
		
	elif(estado[i] == "CA"):
		contca = contca + 1
		i = i + 1
		
	elif(estado[i] == "FL"):
		contfl = contfl + 1 
		i = i + 1
		
	elif(estado[i] == "PA"):
		contpa = contpa + 1
		i = i + 1
		
	elif(estado[i] == "WI"):
		contwi = contwi + 1
		i = i + 1
		
	else:
		conti = conti + 1
		i = i + 1
		
t = array([contaz, contca, contfl, contpa, contwi])
print(max(t))
print(t)
	
			
	




