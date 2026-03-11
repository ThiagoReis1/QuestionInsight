numerodetracajas = int(input("insira o numero inicial de tracajas:"))
taxa_anual = float(input("digite a taxa anual de crescimento:"))
queloniosroubados = int(input("digite o numero de quelonios roubados:"))
i = 1
anos = 0
while (numerodetracajas > 0):
	numerodetracajas = numerodetracajas * ((taxa_anual/100) + 1)
	numerodetracajas = numerodetracajas - 500 - queloniosroubados
	i = i+1
anos = i+1
print (anos)