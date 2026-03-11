civ = int(input("Qual o numero inicial de copias de virus? "))
li = int(input("Qual o numero inicial de leucocitos?"))
tv = float(input("Qual a taxa de variaçao d. do virus? "))
tl = float(input("Qual a taxa de variaçao d. do leucocitos? "))
virus = (civ *tv)
leucocitos = (li * tl)
dias = 1
while(leucocitos < 2 * virus):
	virus = (civ *tv)
	leucocitos = (li * tl)
	df = (dias + 1)
print(df)