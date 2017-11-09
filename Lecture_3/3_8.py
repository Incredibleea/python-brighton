seq1 = ["1","2","3"]
seq2 = ["2","3","4"]

subset = sorted(set(seq1 + seq2))
print(subset)

sub = set(seq1).difference(set(seq2))
sub = sub.union(set(seq2).difference(set(seq1)))
notset = set(seq1+seq2).difference(sub)
print(sorted(notset))

inter = set(seq1).intersection(set(seq2))
print(inter)