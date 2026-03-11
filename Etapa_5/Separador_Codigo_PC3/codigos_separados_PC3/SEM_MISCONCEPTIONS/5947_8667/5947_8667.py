item = input("Digite (C) se deseja coxinha ou (E) se deseja esfirra: ").upper()
quant = int(input("Digite a quantidade de itens: "))
suc = int(input("Digite a quantidade de sucos: "))

if(item == 'C'):
	total=quant*2.0+suc*6.0
	print(total)
else: 
	total=quant*4.5+suc*6.0
	print(total)