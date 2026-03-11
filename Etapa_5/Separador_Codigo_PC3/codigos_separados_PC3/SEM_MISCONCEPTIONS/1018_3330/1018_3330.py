comprimento1=float(input("comprimento do primeiro cateto, em metros: "))
comprimento2=float(input("comprimento do segundo cateto, em metros: "))
custo=float(input("custo de aplicacao do fungicada por metros quadrados: "))
area= (comprimento1 * comprimento2)/2
valortotal= custo*area

print(round(valortotal, 2))