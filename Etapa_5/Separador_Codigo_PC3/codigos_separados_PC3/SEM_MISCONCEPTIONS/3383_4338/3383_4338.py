medida = input("Medida: ")
valor = float(input("Valor da medida: "))

Libras_para_Kg = (valor / 2.20462)
Kg_para_Libras = (valor * 2.20462)
if (medida.upper() == "L"):
	conversao = (Libras_para_Kg)
else:
	conversao = (Kg_para_Libras)
print(round(conversao, 2))