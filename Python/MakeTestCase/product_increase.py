import random
MAX_N1=100
MAX_N2=10**5
MAX_M1=10**5
MAX_M2=10**5
MAX_A=10**5
MAX_B=10**5

output=""
#データセット１(サンプルを含む)
for i in range(8):
    n=random.randint(2,MAX_N1)
    m=random.randint(1,MAX_M1)
    output+=str(n)+" "+str(m)+"\n"
    for j in range(n):
        a=random.randint(1,MAX_A)
        output+=str(a)
        if j!=n-1:
            output+=" "
    output+="\n"
    for j in range(n):
        b=random.randint(0,MAX_B)
        output+=str(b)
        if j!=n-1:
            output+=" "
    output+="\n"
    output+="/\n"

#データセット２
for i in range(20):
    n=random.randint(2,MAX_N2)
    m=random.randint(1,MAX_M2)
    output+=str(n)+" "+str(m)+"\n"
    for j in range(n):
        a=random.randint(1,MAX_A)
        output+=str(a)
        if j!=n-1:
            output+=" "
    output+="\n"
    for j in range(n):
        b=random.randint(0,MAX_B)
        output+=str(b)
        if j!=n-1:
            output+=" "
    output+="\n"
    output+="/\n"
try:
    file_=open("../../TestCase/product_increase.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
