var = input("Resultado da partida: ")
var = var.upper()
somav = 0
somae = 0
v = 3 
e = 1
d = 0
while(var != "X"):
	if(var == "V"):
		somav = somav + v
	elif(var == "E"):
		somae = somae + e
	var = input("Resultado da partida: ")
	var = var.upper()
print(somav)
print(somae)