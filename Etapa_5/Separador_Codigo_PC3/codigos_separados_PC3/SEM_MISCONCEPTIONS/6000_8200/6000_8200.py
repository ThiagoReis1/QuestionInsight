num_cachos = int(input('informe qtdd de cachos:'))

preco_cacho = 5.
preco_desc = 4.25

if num_cachos < 3:
  preco = num_cachos * preco_cacho
else:
  preco = num_cachos * preco_desc

print(round(preco,2))