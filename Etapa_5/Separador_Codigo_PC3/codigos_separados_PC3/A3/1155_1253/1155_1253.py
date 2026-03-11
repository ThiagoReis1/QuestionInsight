#certo numero de virus
numeros_virus = float(input("numero de copias iniciais do virus:"))
# numeros_de_copias_do_virus > numero_leucocitos
numero_leucocitos = float(input("numero de leucocitos:"))
taxa_do_virus = float(input("multiplicaçao diaria do virus (%):"))
taxa_do_leucocitos = float(input("multiplicaçao diaria do leucocitos (%):"))

#quando o numero de leucocitos for 2vezez > que n° de virus estara curada

#variavel acumuladora
numero_leucocitos = 2 * numeros_virus

#variavel contadora
dias = 0

while(numero_leucocitos * 2 <= numeros_virus):
	numero_leucocitos = dias * taxa_do_leucocitos
	numeros_virus = dias * taxa_do_virus
	dias = dias + 1
	print(dias)
	