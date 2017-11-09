# L = [3, 5, 4] ; L = L.sort()
# Metoda sequence.sort() sortuje IN PLACE, wiec bez sensu jest nadpisywanie listy
L = [3, 5, 4] ; L.sort()

# x, y = 1, 2, 3
# przypisanie nastepuje sekwenzyjnie, wiec liczba 3 nie moze byc przypisana

# X = 1, 2, 3 ; X[1] = 4
# X jest obiektem typu tuple, ktory jest niezmienny
X = 1, 2, 3
X = X[0], 4, X[2]
print X

# X = "abc" ; X.append("d")
# X jest obiektem typu string, ktory jest niezmienny

Y = "abc"
Z = Y + "d"
print Z

# map(pow, range(8)) map jako pierwszy argument przyjmuje funkcje lambda
map(lambda x: x**2,range(8))