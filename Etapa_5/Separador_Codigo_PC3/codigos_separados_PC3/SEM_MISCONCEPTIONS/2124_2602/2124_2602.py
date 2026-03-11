from numpy import*
notas = array(eval(input("Digite as notas: ")))
maior = max(notas)
i = 0
new_notas = 0
while (i < size(notas)):
	if (notas[i] < maior):
		new_notas = new_notas + notas[i]
		MFinal = sum(new_notas)/3
	i = i + 1
print (round (MFinal,2))
if (MFinal>5.0):
	print ("APROVOU")
else: 
	print ("REPROVOU")