consumo_chamadas = float(input("consumo por mes:"))
minutos = 0.28 * consumo_chamadas 
fixo = minutos + 23.0
icms = fixo *  0.31
mes =  icms	+ fixo							

print(round(mes, 2))								 
								