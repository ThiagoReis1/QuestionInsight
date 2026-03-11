varx = float(input())
vary = float(input())

if (varx > 0.0 and vary > 0.0):
	print('O ponto (', round(varx,1),',', round(vary,1), ') estah no quadrante 1')
elif (varx < 0.0 and vary > 0.0):
	print('O ponto (', round(varx,1),',', round(vary,1), ') estah no quadrante 2')
elif (varx < 0.0 and vary < 0.0):
	print('O ponto (', round(varx,1),',', round(vary,1), ') estah no quadrante 3')
elif (varx > 0.0 and vary < 0.0):
	print('O ponto (', round(varx,1),',', round(vary,1), ') estah no quadrante 4')
elif (varx == 0.0 and vary == 0.0):
	print('O ponto (', round(varx,1),',', round(vary,1), ') estah situado sobre um dos eixos')
else:
		if(varx == 0.0 and vary != 0.0 or varx != 0.0 and vary == 0.0):
			print('O ponto (', round(varx,1),',', round(vary,1), ') estah sobre um dos eixos')
			
	