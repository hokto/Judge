import random as rd
MAX_N=100
MAX_A=10**9
output=""
for i in range(27):
    n=rd.randint(1,MAX_N)
    output+=str(n)+"\n"
    for j in range(n):
        output+=str(rd.randint(2,MAX_A))
        if j!=n-1:
            output+=" "
    output+="\n"
    output+="/\n"
try:
    file_=open("../TestCase/mprimefact.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
