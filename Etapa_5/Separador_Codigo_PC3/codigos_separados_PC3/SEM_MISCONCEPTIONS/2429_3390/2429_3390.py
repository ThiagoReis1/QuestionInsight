opcao_principal= 6.90
guarnicao= 2.50
bebida= 3.0

n_guar= int(input())
n_beb= int(input())

conta= opcao_principal + (n_guar * guarnicao) + (n_beb * bebida)
conta= float(conta)

print(round(conta,2))