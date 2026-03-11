TS = input("tapioca ou salgado po? ")
quant_TS = float(input("quantos? "))
quant_acai = float(input("quanto acai agora "))

tapioca = 3.5
salgado = 5
acai = 13
					  
if TS == "T":
	conta = quant_TS * tapioca + quant_acai * acai
					  
elif TS == "S":
	conta = quant_TS * salgado + quant_acai * acai
					  
print(conta)