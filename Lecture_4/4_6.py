def sum_seq(seq):
    """Recursive function summing elements in sequence with subsequences"""
    if seq:
        if isinstance(seq[0], (list, tuple)):
            return sum_seq(seq[0])
        else:
            return seq[0] + sum_seq(seq[1:])
    else:
        return 0

print sum_seq.__doc__
print sum_seq([1,2,3,4,5,(1,1,1,1,(2,2))])