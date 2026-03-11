quant_inicial=int(input("quantidade inicial de moedas:"))
desp_mensal=int(input("despesa mensal:"))
quant_M=int(input("quantidade M de moedas de ouro:"))
quant_R=int(input("quantidade R de moedas de ouro:"))
mes=0
while(quant_M>=quant_inicial):
	quant_M=(quant_inicial)-((desp_mensal*mes)+(quant_R*mes))
	mes=mes+1
print(mes)