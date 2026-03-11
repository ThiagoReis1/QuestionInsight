valor= float(input(" "))
opcao= input("D/P/C1/C2:").upper()

if opcao == "D" or opcao == "P":
   total= valor - valor*0.12
	
elif opcao == "C1":
   total= valor
	
else:
	total= valor/0.7-
	
print(round(total,2))