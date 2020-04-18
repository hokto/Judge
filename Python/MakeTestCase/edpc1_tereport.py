import random as rd
MAX_N=10**4
MAX_M=100
output=""
for i in range(28):
    n=rd.randint(1,MAX_N)
    m=rd.randint(1,MAX_M)
    output+=str(n)+" "+str(m)+"\n"
    for j in range(m):
        output+=str(rd.randint(2,n))
        if j!=n-1:
            output+=" "
    output+="\n"
    output+="/\n"
try:
    file_=open("../../TestCase/EDPC1/tereport.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
