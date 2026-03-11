#Entrada de variaveis
unid=input("Qual unidade em que a medida esta? (R/G)")
valor=float(input("Qual o valor do angulo?"))
#unid=unidade em que esta 
#valor= valor do angulo
if unid.upper()=="G" :
	print(round(0.0174533*valor,2))
else:
	print(round(valor/(0.0174533),2))
	