import math,string
def entropy(p):
 cs=0
 if any(c.islower() for c in p): cs+=26
 if any(c.isupper() for c in p): cs+=26
 if any(c.isdigit() for c in p): cs+=10
 if any(c in string.punctuation for c in p): cs+=len(string.punctuation)
 return 0 if cs==0 else len(p)*math.log2(cs)
