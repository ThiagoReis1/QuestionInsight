passagemCli = float(input("Digite o valor da sua passagem: "))
passagemAcom = float(input("Digite o valor da passagem do acompanhante: "))
desconto = passagemAcom - (passagemAcom * (35/100))
total = passagemCli + desconto
print(round(passagemCli,2))
print(round(desconto,2))
print(round(total,2))
