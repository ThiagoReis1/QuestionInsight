from numpy import*

vetor = input("Digite um valor:")
A = 16.75
L = 4.60
P = 2.85
quant_a = 0
quant_l = 0
quant_p = 0
i = 0

while i < len(vetor):
	if vetor[i] == "A":
		quant_a = quant_a + 1
	if vetor[i] == "L":
		quant_l = quant_l + 1
	if vetor[i] == "P":
		quant_p = quant_p + 1
	i = i + 1
total = (quant_a * A) + (quant_l * L) + (quant_p * P)
print(round(total, 2), quant_a, quant_l, quant_p)


