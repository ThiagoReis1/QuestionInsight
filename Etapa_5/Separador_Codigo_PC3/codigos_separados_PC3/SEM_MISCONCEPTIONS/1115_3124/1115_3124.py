salario = float(input())
codigo = int(input())

print("Entradas:","R$",salario,"e","codigo",codigo)

if(salario>0 and codigo==101 or codigo==102 or codigo==103 or codigo==104):
   if(codigo==101):
	   N = salario + (0.80/100)*salario
	   print("Novo salario:","R$",round(N,2))
   elif(codigo==102):
	   N = salario + (0.65/100)*salario
	   print("Novo salario:","R$",round(N,2))
   elif(codigo==103):
	   N = salario + (0.60/100)*salario
	   print("Novo salario:","R$",round(N,2))
   elif(codigo==104):
	   N = salario + (0.55/100)*salario
	   print("Novo salario:","R$",round(N,2))
   else:
      print("Dados invalidos")
else:
	 print("Dados invalidos")
	