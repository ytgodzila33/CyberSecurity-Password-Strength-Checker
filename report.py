from datetime import datetime
def save_report(r):
 with open("password_report.txt","w") as f:
  f.write("CyberShield Report\n")
  for k,v in r.items(): f.write(f"{k}: {v}\n")
  f.write(str(datetime.now()))
