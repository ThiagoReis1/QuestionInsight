coue = input("E coxinha ou esfirra, C ou E? ")
qtd = int(input("Quantos?"))
qtdsucos = int(input("Quantos sucos?"))

if coue.upper() == "C":
	precofinal = 2 * qtd + qtdsucos * 6

else: 
	precofinal = 4.5 * qtd + qtdsucos * 6
	
print(round(precofinal,2))
	