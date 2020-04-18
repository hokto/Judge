import random as rd
MAX_N=10**5
MAX_A=10**9
output=""
for i in range(28):
    n=rd.randint(1,MAX_N)
    output+=str(n)+"\n"
    for j in range(n):
        output+=str(rd.randint(1,MAX_A))
        if j!=n-1:
            output+=" "
    output+="\n"
    output+="/\n"
try:
    file_=open("../../TestCase/EDPC1/max.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
