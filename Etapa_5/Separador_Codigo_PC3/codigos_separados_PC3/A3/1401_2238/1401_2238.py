ataque = input("Tipo de Ataque:")
nb = int(input("Numero de Baforadas:"))

if ataque.lower() == "maritimo":
	dragao = "Viserion"
	uni_mortas = 40 * nb
	
if ataque.lower() == "terrestre":
	dragao = "Drogon"
	uni_mortas = 150 * nb
	
print (dragao)
print (uni_mortas)