consumo=float(input("Digite o seu consumo:"))
total=(consumo*0.43)+10
icms=(total/100)*25
final=icms+total
print(round(final, 2))