import random as rd
MAX_A=10**9
MAX_B=10**9
output=""
for i in range(27):
    a=rd.randint(1,MAX_A)
    b=rd.randint(1,MAX_B)
    output+=str(a)+" "+str(b)+"\n"
    output+="/\n"
try:
    file_=open("../TestCase/dense.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
