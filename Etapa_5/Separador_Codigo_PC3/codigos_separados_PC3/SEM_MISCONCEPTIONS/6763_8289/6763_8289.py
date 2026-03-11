# faça seu código aqui!
tempo = float(input("tempo:"))
taxa = 5.0

if  (tempo < 2) :
	adc = 1.25
elif tempo == 2 :
	adc = 2.25
else:
	adc = 3.25

total = adc + taxa 

print(round(total,2))