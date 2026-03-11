nome = input("Qual o nome do aminoácido? ").upper()
oxi = 15.9994
car = 12.011
nit = 14.0067
hid = 1.00794

if nome == "GLUTAMINA":
	form = car*5+hid*8+nit*1+oxi*4
else:
	form = car*4+hid*9+nit*1+oxi*3
print(round(form,2))