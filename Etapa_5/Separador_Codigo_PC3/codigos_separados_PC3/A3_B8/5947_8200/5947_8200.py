qtdd_cox = 0
qtdd_esf = 0

tipo_salg = input('informequal salgado: (C)oxinha / (E)sfirra ').upper()
qtdd_salg = int(input('quantos salgados ? '))
qtdd_sucos = int(input('quantos sucos ? '))

coxinha = 2.
esfirra = 4.5
suco = 6.

if tipo_salg == "C":
  preco_conta = qtdd_salg * coxinha +qtdd_sucos * suco
else:
  if tipo_salg == "E":
    preco_conta = qtdd_salg * esfirra + qtdd_sucos * suco
		
print(round(preco_conta, 2))
		