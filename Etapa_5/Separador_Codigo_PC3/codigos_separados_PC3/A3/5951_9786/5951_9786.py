tapioca = 4.5
salgado = 5.0 
acai = 12.0 

TouS=(input('Quantidade de salgado:'))
quant_tous= float(input('Quantidade de tapioca:'))
quant_a = float(input('Quantidade de acai:'))


if TouS == 'T': 
   preco_final = (quant_tous * 4.5) + (quant_a * 12.0)
else:
   preco_final = (quant_tous * 5.0) +  (quant_a * 12.0)

print(round(preco_final,2))