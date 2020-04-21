import file_accessor
import subprocess


def run(cmd=None,testcase_inputs=None,outputs_name="",error_index=""):
    run_number=len(testcase_inputs)
    outputs=list()
    for run_i in range(run_number):
        try:
            run_process=subprocess.run(args=cmd,input=testcase_inputs[run_i],
                                        cwd="./",shell=False,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,
                                        timeout=2.0,text=True)
            if run_process.returncode!=0:
                print("Error:caused error in "+str(run_i)+"\n",run_process.stdout)
                return -1
            output=list(run_process.stdout)
            #許容誤差を含むテストケースのフォーマットに合わせて出力を行う 
            #ただし、単体の出力に対応(空白区切りのものなどには未対応)
            if int(error_index)!=0:
                if output[-1]=="\n":
                    output.pop(-1)
                if output[-1]==" ":
                    output.pop(-1)
                output.append("+err("+error_index+")")
                output.append("\n")
            output="".join(output)
            outputs.append(output)
        except subprocess.TimeoutExpired:
            print("TLE in "+str(run_i)+":Confirmation testcase or source")
            return -1
        except Exception as exc:
            print("Exception caused:",exc)
            return -1

    outputs_name="CorrectOutPut/"+outputs_name
    file_accessor.write(file_name=outputs_name,separate_word="/\n",data=outputs,
                        mode="w")
    return 0
if __name__=="__main__":
    print("Input carry out a program command(program need to be compiled)")
    cmd_run=input().split(" ")
    print("Input testcases name need to correct outputs")
    testcase_name=input()
    testcase_name=testcase_name+".txt"
    testcases=file_accessor.read(file_name="TestCase/"+testcase_name,separate_word="/\n")
    if testcases==[]:
        print("FileError:\nTestCase file does not find")
        exit()
    print("Input error of correct output (index)")
    error_index=int(input())
    if error_index>0:
        error_index="+"+str(error_index)
    else:
        error_index=str(error_index)
    #テストケースと正解出力は、別のフォルダに保存するが、名前は同じものにする
    result=run(cmd=cmd_run,testcase_inputs=testcases,outputs_name=testcase_name,
                error_index=error_index)
    if result==0:
        print("Make outputs")
    else:
        print("Caused error and not make outputs")
