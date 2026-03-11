from numpy import*

v1 = input("Tipo de magia: ").upper()
v2 = array(eval(input("Nivel de magia: ")))

i = 0 
dano = 0

while i < size(v2):
	print("1")
	if(v1[i] == "GELO"): 
		dano = dano + 2 * v2[i]
	elif(v1[i] == "FOGO"):
		dano = dano + 3 * v2[i]
	elif(v1[i] == "CHOQUE"):
		dano = dano + 4 * v2[i]
	elif(v1[i] == "CONJURACAO"):
		dano = dano + 8 * v2[i]
	elif(v1[i] == "ILUSAO"):
		dano = dano + 10 * v2[i]
	i = i + 1
print(dano)