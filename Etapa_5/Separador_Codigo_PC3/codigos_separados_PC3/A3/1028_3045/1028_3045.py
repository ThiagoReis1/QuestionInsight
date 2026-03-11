custo = 0.37
taxa_esgoto = 15.00
icms = 35

volume_agua = float(input("Digite o volume de agua consumida: "))

valor = (custo * volume_agua) + taxa_esgoto
valor_icms = valor * (icms / 100) 
resultado = valor + valor_icms
valor_final = print(round(resultado , 2))