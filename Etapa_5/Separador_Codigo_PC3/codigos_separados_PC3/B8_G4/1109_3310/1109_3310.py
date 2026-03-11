#LEIA: IDADE e PESO
# determine a dose 
#adt ou adl a partir de 12 anos, if peso = ou >60kg tomar 1000mg

i = int(input("Digite a idade do paciente: "))
p = float(input("Digite o peso do paciente: "))

print("Entradas:",i,"anos e",p,"kg")

if(0 <= i <=130) and (0.0 <= p <= 550.0):
	if(i>=12 and p >= 60):
		z = 1000
		
	elif(i >= 12 and p < 60):
		z = 875
		
	elif(i<12 and p == 5):
		z = 75
		
	elif(i<12 and 5<p<=9):
		z = 125
		
	elif(i<12 and 9<p<=16):
		z = 250
		
	elif(i<12 and 16<p<=24):
		z = 375
		
	elif(i<12 and 24<p<=30):
		z = 500
		
	elif(i<12 and p>30):
		z = 750
	print("Dosagem:",z,"mg")
		
else:
	print("Dados invalidos")














