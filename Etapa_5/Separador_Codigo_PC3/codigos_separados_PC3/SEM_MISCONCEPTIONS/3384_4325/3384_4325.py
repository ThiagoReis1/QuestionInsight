unid_medida = input("Unidade de medida (O ou K):")
vlr = float(input("Vlr da medida:"))

#conversão
if(unid_medida.upper() == "K"):
	print(round(vlr*35.274,2))
else:
	print(round(vlr/35.274,2))
