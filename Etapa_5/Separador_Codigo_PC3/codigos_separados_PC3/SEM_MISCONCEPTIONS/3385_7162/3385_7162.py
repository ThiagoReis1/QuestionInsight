# MARIA LUÍSA SERRÃO, 05/07

# LEITURA DAS INFORMAÇÕES
unidade = input("Qual unidade de medida? (A/H)")
medida = float(input("Qual o valor da medida?"))
unidade_m = unidade.upper() 

# CÁLCULO
a_h = medida / 2.47105
h_a = medida*2.47105

# SAÍDA
if unidade_m == "A":
	print(round(a_h,2))
else:
	print(round(h_a,2))