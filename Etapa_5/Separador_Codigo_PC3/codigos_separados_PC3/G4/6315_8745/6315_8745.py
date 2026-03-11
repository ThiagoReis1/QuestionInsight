from numpy import*
iogmassal = input("Iogurtes, massa ou salgadinhos: ")
i = 0
iog = 0
mas = 0
sal = 0
s = 0
while i < len(iogmassal):
	if iogmassal[i] == 'I':
		iog = iog + 1
		s = s + 3.75
	if iogmassal[i] == 'M':
		mas = mas + 1
		s = s + 4.50
	if iogmassal[i] == 'S':
		sal = sal + 1
		s = s + 2.90
	i = i + 1
print(round(s, 2),iog,mas,sal)