peso=float(input("digite o peso: "))
kg= 43.21
taxa= 25.00
icms= 62/100
valorfrete= (peso*kg)+taxa
imposto= icms*valorfrete
valortotal= valorfrete+imposto
print(round(valortotal,2))