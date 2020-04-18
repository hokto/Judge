import random as rd
MAX_N1=100
MAX_N2=10**5
output=""
#データセット1(サンプル含む)
for i in range(8):
    n=rd.randint(2,MAX_N1)
    output+=str(n)+"\n"
    v=[i+1 for i in range(n)]
    rd.shuffle(v)
    output+=" ".join([str(i) for i in v])+"\n"
    k=rd.randint(2,n**min(10,n))
    cnt=0
    for j in range(n-1):
        list_=[k for k in range(j+1,n)]
        for k in reversed(list_):
            if v[k]<v[k-1]:
                v[k],v[k-1]=v[k-1],v[k]
                cnt+=1
                if cnt>=k:
                    break
        if cnt>=k:
            break
    output+=" ".join([str(i) for i in v])+"\n"
    output+="/\n"

#データセット2
for i in range(20):
    n=rd.randint(2,MAX_N2)
    output+=str(n)+"\n"
    v=[i+1 for i in range(n)]
    rd.shuffle(v)
    output+=" ".join([str(i) for i in v])+"\n"
    k=rd.randint(2,n**min(10,n))
    cnt=0
    for j in range(n-1):
        list_=[k for k in range(j+1,n)]
        for k in reversed(list_):
            if v[k]<v[k-1]:
                v[k],v[k-1]=v[k-1],v[k]
                cnt+=1
                if cnt>=k:
                    break
        if cnt>=k:
            break
    output+=" ".join([str(i) for i in v])+"\n"
    output+="/\n"
try:
    file_=open("../../TestCase/product_sort.txt","a")
    file_.write(output)
    print("Writed")
except Exception as e:
    print(e)
