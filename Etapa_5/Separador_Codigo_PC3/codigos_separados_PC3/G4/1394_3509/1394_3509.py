hr =float(input("hora de aula"))
if(hr <= 20):
	pg =50*hr
else:
	pg = 50*20+(70*(hr-20))
print(pg)
