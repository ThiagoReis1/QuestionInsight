m = input("c/e: ")
if m.upper()=="C":
	comida = int(input("digite a quantidade de coxinha ou esfirra: "))
	suco = int(input("digite a quantidade de suco: "))
	valorf = (comida * 2)+(suco*6)
else:
	comida = float(input("digite a quantidade de coxinha ou esfirra: "))
	suco = float(input("digite a quantidade de sucos: "))
	valorf =  (comida * 4.50) + (suco* 6)
print(round(valorf,2))