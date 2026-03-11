volume= float(input())
valor_fixo= 15.00
conta= volume * 0.37
conta_com_taxa= conta + valor_fixo
icms= conta_com_taxa * 0.35
valor_a_pagar= conta_com_taxa + icms
valor_a_pagar= float(valor_a_pagar)
print(round(valor_a_pagar,2))