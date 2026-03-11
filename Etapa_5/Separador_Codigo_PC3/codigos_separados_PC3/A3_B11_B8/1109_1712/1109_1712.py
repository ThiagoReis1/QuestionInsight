idade=float(input("qual a idade do paciente: "))
peso=float(input("qual o peso do paciente: "))

if(idade>12 and peso>= 60):
   dosagem = 1000 
elif(peso<60 ):
   dosagem = 875 
elif(idade<12 ):	  
	if(peso<=5 ):
		dosagem = 75
	if(peso>5 and peso<9 ):
		dosagem = 125 
	if(peso>9  and peso<16 ):
		dosagem = 250 
	if(peso>24  and peso<30 ):
		dosagem = 500 
	if(peso>30 ):
	   dosagem = 750 
if(idade<0 and idade>130):
		dosagem = invalida
if(peso<0.0 and peso>550.0):
		dosagem = invalida
	
	