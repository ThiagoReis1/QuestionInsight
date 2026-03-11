plano_fixo = 23.00
minuto = float(input("Quantos minutos voce falou esse mes? "))
fatura = (plano_fixo + (minuto * 0.28)) 
fatura_total = fatura + (fatura*0.31)

print(float(round(fatura_total,2)))