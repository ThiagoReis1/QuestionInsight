coxinha_esfirra = input("digite C para coxinha e E para esfirra: ")
pcoxinha = 2.0
pesfirra = 4.50
psuco = 6.0
if (coxinha_esfirra == "C"):
	
	quantidade_coxinha = int(input("quantidade de coxinha: "))
	quantidade_suco = int(input("quantidade de suco: "))
	
	total = (quantidade_coxinha * pcoxinha) + (quantidade_suco * psuco)
	print(round(total, 2))
else:
	quantidade_esfirra = int(input("quantidade de esfirra: "))
	quantidade_suco = int(input("quantidade de suco:"))
	total = (quantidade_esfirra * pesfirra) + (quantidade_suco * psuco)
	print(round(total,2))