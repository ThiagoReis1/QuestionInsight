tempo_lig = float(input("Qnt tempo vc ficou em ligacao: "));
valor_minuto = 0.28
consumo = tempo_lig * valor_minuto;
valor_fixo = 23;
icms = 31 / 100;
custo_1 = ((consumo) + (valor_fixo))
custo_2 = custo_1 + custo_1 * icms
print(round(custo_2, 2))