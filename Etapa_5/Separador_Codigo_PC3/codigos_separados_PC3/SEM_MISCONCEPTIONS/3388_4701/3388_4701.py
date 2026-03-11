unidade = input("unidade: ")
valor= float(input("valor : "))
unidade1= unidade.upper()

btu= 3.41214*valor
watt= valor/3.41214

if(unidade1=='W'):
		
		
		print(round(btu,2))
if(unidade1=='B'):
		
		
		print(round(watt,2))
