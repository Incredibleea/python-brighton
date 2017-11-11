def printRuler(number):
    """Function printing ruler"""
    line = "|...." * number + "|" + "\n0"
    for i in range(1,number+1):
        line += str(i).rjust(5)
    print line

def printCross(height=1,width=1):
    """Function printing cross"""
    primaryRow = "+" + "---+" * width + "\n|" + "   |" * width + "\n+" + "---+" * width
    secondaryRow = "\n|" + "   |" * width + "\n+" + "---+" * width

    line = primaryRow
    for i in range(height-1):
        line += secondaryRow

    print(line)

print printRuler.__doc__
printRuler(4)
print printCross.__doc__
printCross(2,5)