# faça seu códigod
dias_consecutivos = int(input("insira os dias"))
diaria = 100
if dias_consecutivos < 7:
   print(round(dias_consecutivos * 100 + 15, 2))
elif dias_consecutivos == 7:
	print(round(dias_consecutivos * 100 + 12, 2))
elif dias_consecutivos > 7:
	print(round(dias_consecutivos * 100 + 10, 2))