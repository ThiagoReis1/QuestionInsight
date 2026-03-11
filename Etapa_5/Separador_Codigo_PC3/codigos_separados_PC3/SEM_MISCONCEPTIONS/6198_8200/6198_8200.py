altura_luna = 1.65
taxa_luna = 0.02
ctd = 0
h_pessoa = float(input('qual altura: '))
tx_pessoa = float(input('qual taxa crescimento: '))

while altura_luna < h_pessoa:
  altura_luna = altura_luna + taxa_luna 
  h_pessoa = h_pessoa + tx_pessoa
  ctd += 1
	
print(ctd)