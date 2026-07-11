from analyzer import analyze_password
from generator import generate_password
from report import save_report
name=input("Name: ")
pw=input("Password: ")
res=analyze_password(name,pw)
for k,v in res.items(): print(f"{k}: {v}")
if res["Strength"]=="Weak":
    print("Suggested:",generate_password())
save_report(res)
