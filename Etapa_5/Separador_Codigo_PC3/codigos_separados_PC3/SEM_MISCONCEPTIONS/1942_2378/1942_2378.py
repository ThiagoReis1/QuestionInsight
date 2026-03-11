#Universidade Federal do Amazonas
#Caio Sombra

aminoacido = input("digite qual aminoacido: ")

o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

histidina = (6*c + 10*h + 3*n + 2*o)
prolina = (5*c + 10*h + n + 2*o)

if(aminoacido == "histidina"):
	soma = histidina
else:
	soma = prolina
	
print(round(soma, 2))