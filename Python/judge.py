import file_accessor
import subprocess

def decision(cmd=None,input_="",correct_output=""):
    try:
        process_res=subprocess.run(args=cmd,input=input_,cwd="./",shell=False,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,timeout=2.0,text=True)

        status,output=process_res.returncode,process_res.stdout
        #改行前に余計な空白があった場合は、削除
        #(正解用出力、判定する出力どちらにも対応させている)
        output_split=list(output)
        if output_split[-2]==" ":
            output_split.pop(-2)
        output="".join(output_split)
        correct_output_split=list(correct_output)
        if correct_output_split[-2]=="":
            correct_output.pop(-2)
        correct_output="".join(correct_output_split)
        #REだった場合
        if status==1:
            return 3

        #ACだった場合
        if output==correct_output:
            return 0
        #WAだった場合
        else:
            return 1
    #TLE(制限時間2sec)だった場合
    except subprocess.TimeoutExpired:
        return 2
    
def run_cpp(object_file_name="",testcase_inputs=None,correct_outputs=None):
    ac,wa,tle,re,ce=[0]*5
    run_number=len(testcase_inputs)
    cmd_compile=["g++",object_file_name,"-o","main.out"]
    process_res=subprocess.run(args=cmd_compile,cwd="./",shell=False,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT) 
    status_compile,error_b=process_res.returncode,process_res.stdout
    #CEだった場合
    if status_compile==1:
        print("CE:",error_b.decode("utf8"))
        ce=run_number
        return ac,wa,tle,re,ce
    cmd_cpp=["./main.out"]
    for run_i in range(run_number):
        run_result=decision(cmd=cmd_cpp,input_=testcase_inputs[run_i],
                            correct_output=correct_outputs[run_i])
        if run_result==0:
            print(run_i,":AC")
            ac+=1
        elif run_result==1:
            print(run_i,":WA")
            wa+=1
        elif run_result==2:
            print(run_i,":TLE")
            tle+=1
        elif run_result==3:
            print(run_i,":RE")
            re+=1
    return ac,wa,tle,re,ce


def run_ruby(object_file_name="",testcase_inputs=None,correct_outputs=None):
    ac,wa,tle,re,ce=[0]*5
    run_number=len(testcase_inputs)
    cmd_rb=["ruby",object_file_name]
    for run_i in range(run_number):
        run_result=decision(cmd=cmd_rb,input_=testcase_inputs[run_i],
                            correct_output=correct_outputs[run_i])        
        if run_result==0:
            print(run_i,":AC")
            ac+=1
        elif run_result==1:
            print(run_i,":WA")
            wa+=1
        elif run_result==2:
            print(run_i,":TLE")
            tle+=1
        elif run_result==3:
            print(run_i,":RE")
            re+=1
    return ac,wa,tle,re,ce


def run_python(object_file_name="",testcase_inputs=None,correct_outputs=None):
    ac,wa,tle,re,ce=[0]*5
    run_number=len(testcase_inputs)
    cmd_py=["python3",object_file_name]
    for run_i in range(run_number):
        run_result=decision(cmd=cmd_py,input=testcase_inputs[run_i],
                            correct_output=correct_outputs[run_i])        
        if run_result==0:
            print(run_i,":AC")
            ac+=1
        elif run_result==1:
            print(run_i,":WA")
            wa+=1
        elif run_result==2:
            print(run_i,":TLE")
            tle+=1
        elif run_result==3:
            print(run_i,":RE")
            re+=1
    return ac,wa,tle,re,ce


def run(object_file_name="",testcase_inputs=None,correct_outputs=None):
    #テストケースと正解出力ファイルの数が同じでなければ実行させない
    if len(testcase_inputs)!=len(correct_outputs):
        print("Size Error:\nTestCase's size is ",len(testcase_inputs),"but",
            "CorrectOutPut's size is ",len(correct_outputs),".\n"
            +"Please check TestCase file and CorrectOutPut file.")
        return [-1]*5
    #拡張子だけ取り出したいから右から分割
    extension=object_file_name.rsplit(".",1)[1]
    ac,wa,tle,re,ce=[0]*5
    #ジャッジする言語が増えればここに関数の追加
    if extension=="cpp":
        ac,wa,tle,re,ce=run_cpp(object_file_name,testcase_inputs,
                                correct_outputs)
    elif extension=="rb":
        ac,wa,tle,re,ce=run_ruby(object_file_name,testcase_inputs,
                                correct_outputs)
    elif extension=="py":
        ac,wa,tle,re,ce=run_python(object_file_name,testcase_inputs,
                                    correct_outputs)
    
    #最終結果を優先度順を考慮して分岐
    print("Result:",end="")
    if ce!=0:
        print("CE")
    elif wa!=0:
        print("WA")
    elif tle!=0:
        print("TLE")
    elif re!=0:
        print("RE")
    else:
        print("AC")
    return ac,wa,tle,re,ce

if __name__=="__main__":
    print("Input decision name")
    decision_name=input()
    print("Input judged source name")
    file_name=input()
    #区切り文字はまだ未決定なので仮置き
    testcases=file_accessor.read(file_name="./TestCase/"+str(decision_name)+".txt",
                        separate_word="/\n")
    #テストケースが見つからなかったら強制終了
    if testcases==[]:
        print("FileError:\nTestCase file does not find")
        exit()
    correct_outputs=file_accessor.read(file_name="./CorrectOutPut/"+str(decision_name)+".txt",
                              separate_word="/\n")
    #正解出力ファイルが見つからなかったら強制終了
    if correct_outputs==[]:
        print("FileError:\nCorrectOutPut file does not find")
        exit()
    ac,wa,tle,re,ce=run(object_file_name=file_name,testcase_inputs=testcases,
                        correct_outputs=correct_outputs)
    print(ac,wa,tle,re,ce)

