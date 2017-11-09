'''i = raw_input('Podaj dlugosc miarki:')'''

number = 4
line = "|...." * number + "|" + "\n0"
for i in range(1,number+1):
    line += str(i).rjust(5)
print line