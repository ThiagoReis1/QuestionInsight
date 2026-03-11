qt_laranja = int(input('quantidade de laranja:'))

if qt_laranja >= 6:
	unidade = 0.60
else:
	unidade = 0.75
total = qt_laranja * unidade
print(round(total, 2))
