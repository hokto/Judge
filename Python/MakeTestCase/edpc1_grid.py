import random as rd
MAX_H=10**3
MAX_W=10**3
C="....#"
output=""
for i in range(28):
    h=rd.randint(1,MAX_H)
    w=rd.randint(1,MAX_W)
    output+=str(h)+" "+str(w)+"\n"
    c=[["" for j in range(w)] for k in range(h)]
    c[rd.randint(0,h-1)][rd.randint(0,w-1)]="s"
    while True:
        gw=rd.randint(0,w-1)
        gh=rd.randint(0,h-1)
        if c[gh][gw]!="s":
            c[gh][gw]="g"
            break

    for y in range(h):
        for x in range(w):
            if c[y][x]!="":
                continue
            c[y][x]="".join(rd.choices(C,k=1))
    for j in range(h):
        for k in range(w):
            output+=c[j][k]
        output+="\n"
    output+="/\n"

try:
    file_=open("../../TestCase/EDPC1/grid.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
