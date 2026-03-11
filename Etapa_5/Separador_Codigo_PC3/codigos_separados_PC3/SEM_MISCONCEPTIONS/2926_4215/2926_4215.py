acai=float(input("Quandidade de acai no copo(em gramas): "))
esfirras=int(input("Quantidade de esfirras: "))

valor_das_esfirras=esfirras*3.0
valor_do_acai=acai*0.001*24.0
valor_total=valor_das_esfirras+valor_do_acai
print(round(valor_total,2))