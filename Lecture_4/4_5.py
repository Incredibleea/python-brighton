def odwracanie(L, left, right):
    """Function returning list with inverted elements at indexes <left,right>"""
    sublist = list(L[left:right+1])
    sublist.reverse()
    return L[:left] + sublist + L[right+1:]

def odwracanieR(L,left,right):
    """Recursive function returning list with inverted elements at indexes <left,right>"""
    if left != right and left < right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        return odwracanieR(L,left+1,right-1)
    else:
        return L

print odwracanie.__doc__
print odwracanie([1,2,3,4,5,6,7],2,6)

print odwracanieR.__doc__
print odwracanieR([1,2,3,4,5,6,7],2,6)