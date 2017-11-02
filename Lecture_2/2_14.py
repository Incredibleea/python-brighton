import operator

line = "Dzisiaj jest mecz Ligi Mistrzow"
linelist = line.split()
linelist.sort(key=len, reverse=True)
print('{} : {}'.format(linelist[0],len(linelist[0])))