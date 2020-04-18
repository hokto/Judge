import random as rd
MAX_S=10**3
MAX_T=10**3
output=""
LETTERS="abcdefghijklmnopqrstuvwxyz"
for i in range(27):
    s=rd.randint(1,MAX_S)
    t=rd.randint(1,MAX_T)
    output+="".join(rd.choices(LETTERS,k=s))+"\n"
    output+="".join(rd.choices(LETTERS,k=t))+"\n"
    output+="/\n"
try:
    file_=open("../../TestCase/EDPC1/levenstein.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
