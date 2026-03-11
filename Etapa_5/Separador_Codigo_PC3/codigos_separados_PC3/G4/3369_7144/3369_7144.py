v = input("Digite em qual unidade esta em K ou M: ")
ve = float(input("Digite o valor da velocidade: "))

if(v == "K"):
   vkm = ve / 3.6
   print(round(vkm, 2))
else:
   vm = 3.6 * ve
   print(round(vm, 2))

