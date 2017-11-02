line = "Kobyla ma maly bok"
alphabeticallySorted = sorted(line.split(), cmp=lambda x,y: cmp(x.lower(),y.lower()))
print alphabeticallySorted
lenSorted = sorted(line.split(), key=len, reverse=True)
print lenSorted