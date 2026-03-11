est_arv = float(input('estimativa de arvore'))
comp_lado = float(input('comprimento do lado'))
b = 10*(5**0.5)
c = (25+b)**0.5
area = ((comp_lado**2)*c)/4
total = area*est_arv
print(int(total))

		  