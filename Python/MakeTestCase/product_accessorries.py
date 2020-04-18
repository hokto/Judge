import random
MAX_N=10**3
MAX_M=10**3
MAX_A=10**9
MAX_X=MAX_N
MAX_Y=10**9
output=""
for i in range(28):
    n=random.randint(1,MAX_N)
    m=random.randint(1,MAX_M)
    output+=str(n)+" "+str(m)+"\n"
    for j in range(n):
        output+=str(random.randint(1,MAX_A))
        if j!=n-1:
            output+=" "
    output+="\n"
    for j in range(m):
        x=random.randint(1,n)
        if x>n:
            print("Over!!")
            exit()
        y=random.randint(1,MAX_Y)
        output+=str(x)+" "+str(y)+"\n"
    output+="/\n"
try:
    file_=open("../../TestCase/product_accessories.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
