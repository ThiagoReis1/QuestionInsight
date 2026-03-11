plano_top= 45.00
fon=float(input("excedentes:"))
excedente_bad= 0.97*fon
a= plano_top+excedente_bad
icms_ladrao= a*42/100
total=a+icms_ladrao
print(round(total,2))