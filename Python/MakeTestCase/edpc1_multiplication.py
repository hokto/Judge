import random as rd
MAX_N=10**4
MAX_M=100
MAX_K=10**4
output=""
for i in range(28):
    n=rd.randint(1,MAX_N)
    m=rd.randint(1,MAX_M)
    k=rd.randint(1,MAX_K)
    output+=str(n)+" "+str(m)+" "+str(k)+"\n"
    for j in range(m):
        output+=str(rd.randint(2,n))
        if j!=n-1:
            output+=" "
    output+="\n"
    for j in range(k):
        output+=str(rd.randint(1,n))
        if j!=n-1:
            output+=" "
    output+="\n"
    output+="/\n"

try:
    file_=open("../../TestCase/EDPC1/multiplication.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
