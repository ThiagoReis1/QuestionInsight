comprinha = float(input("valor da compra: "))
codiguin = input("qual o codigo mermao: D, P ou C: ")

if codiguin == 'D':
	total = comprinha - (comprinha*0.18)
elif codiguin == 'P':
	total = comprinha - (comprinha*0.18)
elif codiguin == 'C':
	vzs = int(input("quantas vezes: "))
	if vzs == 1:
 	   total = comprinha
	elif vzs == 2:
		total = comprinha + (comprinha*0.07)
print(round(total, 2))