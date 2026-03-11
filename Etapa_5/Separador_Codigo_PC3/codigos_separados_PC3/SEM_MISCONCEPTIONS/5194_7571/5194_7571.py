missao= input("classe A ou B: ").upper()
valor= float(input("digite o valor: "))

if(missao=="B"):
	print("Classe: Chunin")
	imposto= valor*(15/100)
	vlfinal= valor-imposto
	print(round(vlfinal,2))
	
if(missao=="A"):
	print("Classe: Jounin")
	imposto= valor*(22/100)
	vlfinal= valor-imposto
	print(round(vlfinal, 2))
	