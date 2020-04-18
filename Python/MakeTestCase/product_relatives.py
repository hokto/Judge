import random as rd
MAX_N2=10**5
MAX_M2=2*10**5
MAX_N1=100
MAX_M1=100

output=""
#データセット1(サンプル含む)
for i in range(8):
    n=rd.randint(2,MAX_N1)
    m=rd.randint(1,MAX_M1)
    output+=str(n)+" "+str(m)+"\n"
    for j in range(m):
        x=None
        y=None
        while True:
            x=rd.randint(1,n)
            y=rd.randint(1,n)
            if x!=y:
                break
        output+=str(x)+" "+str(y)+"\n"
    output+="/\n"

#データセット2
for i in range(20):
    n=rd.randint(2,MAX_N2)
    m=rd.randint(1,MAX_M2)
    output+=str(n)+" "+str(m)+"\n"
    for j in range(m):
        x=None
        y=None
        while True:
            x=rd.randint(1,n)
            y=rd.randint(1,n)
            if x!=y:
                break
        output+=str(x)+" "+str(y)+"\n"
    output+="/\n"
try:
    file_=open("../../TestCase/product_relatives.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
