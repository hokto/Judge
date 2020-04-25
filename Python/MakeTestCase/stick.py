import random as rd
MAX_N=100
MAX_L=50
output=""
for i in range(27):
    n=rd.randint(1,MAX_N)
    output+=str(n)+"\n"
    for j in range(n):
        output+=str(rd.randint(1,MAX_L))
        if j!=n-1:
            output+=" "
    output+="\n"
    output+="/\n"
try:
    file_=open("../TestCase/stick.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
