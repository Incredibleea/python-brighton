x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

# kod jest ok, sredniki na koncu mozna usunac

'''for i in "qwerty": if ord(i) < 100: print i'''
for i in "qwerty":
    if ord(i) < 100: print i
    
# if nie miesci sie w bloku funkcji for, musi zostac przesuniete do nowej linii

for i in "axby": print ord(i) if ord(i) < 100 else i

# jest ok

x, y, z = 2,3,5

print x
print y,z 