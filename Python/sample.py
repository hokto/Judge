import subprocess

#res1=subprocess.run(["g++","test.cpp","-o","test.out"],cwd="./",shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
res1=subprocess.run(args=["ruby","test.rb"],cwd="./",shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

print(res1)
try:
    res2=subprocess.run(["./test.out"],cwd="./",shell=False,input="10",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=2,text=True)
    print(res2)
except subprocess.TimeoutExpired:
    print("TimeOut!")
