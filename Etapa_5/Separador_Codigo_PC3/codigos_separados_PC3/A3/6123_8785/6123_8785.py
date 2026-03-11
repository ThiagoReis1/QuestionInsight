salto= int(input())
combustivel=0

if salto <+ 17.5:
	total= salto + 0.8
elif salto >= 17.5 and salto <= 35.0:
	total= salto + 1.3
elif salto > 35.0 and salto <= 50.0:
	total= salto + 2.1
else:
	total= salto + 3.0
	
print(total)