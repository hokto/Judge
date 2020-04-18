import random as rd
MAX_N1=100
MAX_N2=10**5
MAX_M1=100
MAX_M2=10**4
MAX_A=10**9
MAX_X=10**9

output=""
#データセット1(サンプルを含む)
for i in range(8):
    n=rd.randint(2,MAX_N1)
    m=rd.randint(1,MAX_M1)
    output+=str(n)+" "+str(m)+"\n"
    for j in range(n):
        a=rd.randint(1,MAX_A)
        output+=str(a)
        if j!=n-1:
            output+=" "
    output+="\n"
    for j in range(m):
        l=rd.randint(1,n-1)
        r=rd.randint(l+1,n)
        x=rd.randint(1,MAX_A)
        output+=str(l)+" "+str(r)+" "+str(x)+"\n"
    output+="/\n"

#データセット2
for i in range(20):
    n=rd.randint(2,MAX_N2)
    m=rd.randint(1,MAX_M2)
    output+=str(n)+" "+str(m)+"\n"
    for j in range(n):
        a=rd.randint(1,MAX_A)
        output+=str(a)
        if j!=n-1:
            output+=" "
    output+="\n"
    for j in range(m):
        l=rd.randint(1,n-1)
        r=rd.randint(l+1,n)
        x=rd.randint(1,MAX_A)
        output+=str(l)+" "+str(r)+" "+str(x)+"\n"
    output+="/\n"

try:
    file_=open("../../TestCase/product_range_increase.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
