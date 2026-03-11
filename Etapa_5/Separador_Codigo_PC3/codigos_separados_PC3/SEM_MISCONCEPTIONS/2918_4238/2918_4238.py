precoIngresso=float(input())
ingressos=float(input())
precoPromocional=precoIngresso-(precoIngresso*(20/100))
total=precoPromocional*ingressos
print(round(total,2))