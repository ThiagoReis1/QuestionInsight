numb = int(input("numero de bacteria: "))
horas = int(input("numeros de horas: "))
			  
cont = 0 
soma = numb
			  
while( cont < horas):
	soma = int((2/100) * soma) + soma 
	cont = cont + 1 
	
	
print(soma)
      