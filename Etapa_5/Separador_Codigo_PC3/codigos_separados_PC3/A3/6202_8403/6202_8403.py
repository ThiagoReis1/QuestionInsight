altura_bia = 1.69
taxa_bia = 0.01



alt = float(input('Altura:'))
taxa = float(input('Taxa:'))
c = 0



while alt > 0 and taxa > 0:
   if altura_bia > alt:
      c = alt + taxa
print(c)	
