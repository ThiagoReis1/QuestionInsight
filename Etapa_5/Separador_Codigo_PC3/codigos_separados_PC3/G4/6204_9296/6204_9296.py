altm = 1.86
taxm = 0.01
cont = 0
altc = float(input("Qual a altura do coelho?"))
taxc = float(input("Qual a taxa do coelho? "))

while(altc < altm):
	altm = altm + taxm
	altc = altc + taxc
	cont = cont + 1
print(cont)