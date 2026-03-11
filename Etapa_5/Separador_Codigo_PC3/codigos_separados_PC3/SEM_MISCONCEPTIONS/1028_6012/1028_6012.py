vol = float(input("volume consumido: "))
string = (vol * 0.37) + 15
conta =  string * 35 / 100
total = string + conta
print(round(total, 2))