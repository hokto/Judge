import file_accessor
import subprocess


def run(cmd=None,testcase_inputs=None,outputs_name=""):
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
            outputs.append(run_process.stdout)
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
    #テストケースと正解出力は、別のフォルダに保存するが、名前は同じものにする
    result=run(cmd=cmd_run,testcase_inputs=testcases,outputs_name=testcase_name)
    if result==0:
        print("Make outputs")
    else:
        print("Caused error and not make outputs")
