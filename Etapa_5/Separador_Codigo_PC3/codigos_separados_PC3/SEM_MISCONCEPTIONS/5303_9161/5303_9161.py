massa = int(input("massa (gramas) : "))
massa_tax = 0.10 # perde 10% da massa ao ano

cont = 0
while massa >= 0.5 :
	massa = massa - massa*massa_tax
	cont += 1
print(cont)
	