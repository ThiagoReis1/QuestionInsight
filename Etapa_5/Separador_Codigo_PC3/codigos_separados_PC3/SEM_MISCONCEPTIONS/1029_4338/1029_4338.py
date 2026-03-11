vlr_minuto = 0.28 #Valor fixo por minuto de chamada
vlr_fixo = 23 #Valor fixo de assinatura
icms = 31/100

consumo= float(input("Consumo em minutos: "))
acrescimo_icms= (((vlr_minuto * consumo) + vlr_fixo) * icms)
vlr_a_pagar = (((consumo * vlr_minuto) + vlr_fixo) + acrescimo_icms)


print(round(vlr_a_pagar, 2))