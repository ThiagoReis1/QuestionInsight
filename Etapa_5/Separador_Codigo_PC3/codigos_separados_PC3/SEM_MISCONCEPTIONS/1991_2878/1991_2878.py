entrada = input("Digite o nome do aminoacido: ")

if(entrada.upper() == "GLICINA"):
	soma = ((12.011 * 2) + (1.0079 * 5) + (14.00674 +(15.9995 * 2))) 
	print(round(soma, 2))
elif(entrada.upper() == "PROLINA"):
   soma = ((12.011 * 5) + (1.0079 * 10) + (14.00674 +(15.9995 * 2)))
   print(round(soma, 2))
elif(entrada.upper() == "SERINA"):
   soma = ((12.011 * 3) + (1.0079 * 7) + (14.00674 +(15.9995 * 3))) 
   print(round(soma, 2))
else:
   print("Entrada:", entrada)
   print("Dado Invalido")