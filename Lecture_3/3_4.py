def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        print 'Bad value'
        return False

while True:
    x = raw_input("Podaj liczbe: ")
    if is_number(x):
        print x, pow(x,3)
    elif x == "stop":
        break