# faça seu código aqui!
qntdedias = float(input("quantidade dias que um cliente deseja alugar um carro: "))

if qntdedias - 7:
	print(round(qntdedias * 100 + 10  , 2 ))
elif qntdedias == 7:
	print(round((qntdedias * 100) + 12  , 2 ))
else:
	qntdedias + 7 
	print(round((qntdedias * 100 + 15) , 2 ))