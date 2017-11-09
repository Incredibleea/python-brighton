height = 3
width = 15
primaryRow = "+" + "---+" * width + "\n|" + "   |" * width + "\n+" + "---+" * width
secondaryRow = "\n|" + "   |" * width + "\n+" + "---+" * width

line = primaryRow
for i in range(height-1):
    line += secondaryRow

print(line)