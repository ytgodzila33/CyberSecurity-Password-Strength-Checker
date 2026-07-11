from entropy import entropy
from utils import common,dictionary
import re,string
def analyze_password(name,p):
 s=0;w=[]
 if len(p)>=12:s+=20
 elif len(p)>=8:s+=10
 u=any(c.isupper() for c in p);l=any(c.islower() for c in p);d=any(c.isdigit() for c in p);sy=any(c in string.punctuation for c in p)
 s+=15*u+15*l+15*d+20*sy
 if p.lower() in common:w+=["Common password"]
 if any(x in p.lower() for x in dictionary):w+=["Dictionary word"]
 if name.lower() in p.lower():w+=["Contains name"]
 if re.search(r'(.)\1\1',p):w+=["Repeated chars"]
 e=entropy(p)
 if not w:s+=15
 st="Weak" if s<50 else "Medium" if s<80 else "Strong"
 return {"Score":s,"Entropy":round(e,2),"Strength":st,"Warnings":", ".join(w) or "None"}