#custo plano celular = 45 reais
#0,97 centavos por minutos
#42% de imposto do total a mais

v=float(input("Informe os minutos excedentes de um mes:"))
cp= (v*0.97)+45.00 #custo primario
imposto= cp*0.42
ct= cp+imposto
print(round(ct, 2))