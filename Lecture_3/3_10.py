def roman2int(romanic):
    total = 0
    while romanic:
        firstNum    = romans[romanic[0]]
        if len(romanic)>1:
            secondNum   = romans[romanic[1]] 
        else:
            -1
        if firstNum >= secondNum:
            total += firstNum
            romanic = romanic[1:]
        else:
            total += (secondNum - firstNum)
            romanic = romanic[2:]
    print(total)

romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500}
romans['M'] = 1000

roman2int("MMCXXXIV")