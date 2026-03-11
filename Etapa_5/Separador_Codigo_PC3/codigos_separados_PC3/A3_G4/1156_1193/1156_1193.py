num = int(input("Numero inicial de celulas cancerosas: "))
taxa_percentual = float(input("Taxa percentual (em %) de reducao do cancer: "))
novas_celulas = int(input("Numero de novas celulas cancerosas: "))
t = 1
cel = num
w = 0
soma = cel + novas_celulas
while (soma >= 500000):
	w = w + soma 
	t = t + 1
print()