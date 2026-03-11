from numpy import*

freq = array(eval(input("Quais as freq: ")))
rep_freq = 0
situacao = zeros(rep_freq, dtype=int)
j = 0
freq_porc = freq[j] / 100
freq_nec = 0.70


for i in range (size(freq)):
	if freq_porc < freq_nec:
		rep_freq = rep_freq + 1
	j = j + 1
print(rep_freq)

	
	
	