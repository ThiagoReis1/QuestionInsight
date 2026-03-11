escala= input('escala: ').upper()
t= float(input('valor da temperatura: '))

if escala=="C":
	temp=t+273.15
else:
	temp=t-273.15

print(round(temp,2))