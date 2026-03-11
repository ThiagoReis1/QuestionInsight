consumo = float(input("Quantos minutos voce consumiu o plano ? "))

plano = 0.28
varfixo = 23.00
icms = 0.31

taxa = ((consumo * plano) + varfixo) * 0.31

varF = ((consumo * plano) + varfixo) + taxa

print(round(varF, 2))					 