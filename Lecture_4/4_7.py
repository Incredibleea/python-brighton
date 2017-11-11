def flatten(seq):
    """Recursive function making elements in sequence with subsequences flat"""
    if seq != []:
        if isinstance(seq[0], list):
            return flatten(seq[0]) + flatten(seq[1:])
        elif isinstance(seq[0], tuple):
            return flatten(list(seq[0])) + flatten(seq[1:]) 
        else:
            return seq[:1] + flatten(seq[1:])
    else:
        return seq

print flatten.__doc__
print flatten([1,2,3,[[1],2,3],4,5,[1,1,1,1],(7,8,(88,(99,111)))])