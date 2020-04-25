import file_accessor
import subprocess
import re


def is_unadulterated_match(output=None,correct_output=None):
    #ACだった場合
    if output==correct_output:
        return 0
    #WAだった場合
    else:
        return 1

def is_permissible_error(output=None,correct_output=None):
    #誤差の計算処理
    #正規表現を用いて必要な情報を抽出
    #例:10+err(-5) <= (10-1e-5 <= X <= 10+1e-5)を満たすXが範囲内誤差
    error_str=re.findall(r"\+err\([\+\-]\d+\)",correct_output)[0]
    error_int=int(re.findall(r"[\+\-]\d+",error_str)[0])
    criterion=float(re.sub(r"(\+err\([\+\-]\d+\))","",correct_output))
    permissible_error_min=criterion-10**error_int
    permissible_error_max=criterion+10**error_int
    output_float=float(output)
    #許容誤差範囲内ならばAC
    if permissible_error_min<=output_float<=permissible_error_max:
        return 0
    else:
        return 1

def is_alternative_match(input_="",output="",judgecommand=""):
    cmd=re.sub(r"judgecommand\(|\)","",judgecommand)
    cmd_split=cmd.split(" ")
    process_res=subprocess.run(args=cmd_split,input=input_+output,cwd="./",shell=False,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,text=True)
    status,output=process_res.returncode,process_res.stdout
    #ジャッジするプログラムでエラーが吐かれるなら提出コードが間違いであると判断
    if status==1:
        return 1
    #ジャッジするプログラムが1(WA)か0(AC)を出力するのでそれを返す
    return int(output)
def decision(cmd=None,input_="",correct_output=""):
    try:
        process_res=subprocess.run(args=cmd,input=input_,cwd="./",shell=False,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,timeout=2.0,text=True)

        status,output=process_res.returncode,process_res.stdout
        #改行前に余計な空白があった場合は、削除
        #(正解用出力、判定する出力どちらにも対応させている)
        output_split=list(output)
        if output_split[-1]=="\n":
            output_split.pop(-1)
        if output_split[-1]==" ":
            output_split.pop(-1)
        output="".join(output_split)
        correct_output_split=list(correct_output)
        if correct_output_split[-1]=="\n":
            correct_output_split.pop(-1)
        if correct_output_split[-1]==" ":
            correct_output_split.pop(-1)
        correct_output="".join(correct_output_split)
        #REだった場合
        if status==1:
            return 3

        #ここで処理しないとのちの処理で文字列が分割される
        if re.fullmatch(r'judgecommand\(.+\)', correct_output) is not None:
            return is_alternative_match(input_,output,correct_output)
        separate_word=None
        if " " in correct_output:
            correct_output=correct_output.split(" ")
            separate_word=" "
        elif "\n" in correct_output:
            correct_output=correct_output.split("\n")
            separate_word="\n"
        #１つの出力のみと判断して単体のジャッジを行う
        if separate_word is None:
            #誤差を許容するテストケースの場合、判定方法を変える
            if re.fullmatch(r'.+\+err\([\+\-]\d+\)',correct_output) is not None:
                return is_permissible_error(output,correct_output)
            else:
                return is_unadulterated_match(output,correct_output)
        else:
        #複数ある場合は、それぞれでジャッジを行う
            correct_output_number=len(correct_output)
            output=output.split(separate_word)
            if correct_output_number!=len(output):
                return 1
            else:
                judge_result=-1
                for output_i in range(correct_output_number):
                    #誤差を許容するテストケースの場合、判定方法を変える
                    if re.fullmatch(r'.+\+err\([\+\-]\d+\)',correct_output[output_i])\
                            is not None:
                        judge_result=is_permissible_error(output[output_i],
                                                        correct_output[output_i])
                    else:
                        judge_result=is_unadulterated_match(output[output_i],
                                                        correct_output[output_i])
                    #どれか１つでもWAならばその時点で結果はWAとなる
                    if judge_result==1:
                        return 1
                return 0
    #TLE(制限時間2sec)だった場合
    except subprocess.TimeoutExpired:
        return 2
    
def run_cpp(object_file_name="",testcase_inputs=None,correct_outputs=None,allotment=None):
    ac,wa,tle,re,ce=[0]*5
    run_number=len(testcase_inputs)
    cmd_compile=["g++",object_file_name,"-o","main.out"]
    process_res=subprocess.run(args=cmd_compile,cwd="./",shell=False,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT) 
    status_compile,error_b=process_res.returncode,process_res.stdout
    point=0
    #結果をまとめて返す
    res=""
    #CEだった場合
    if status_compile==1:
        res+="CE:"+error_b.decode("utf8")
        ce=run_number
        return ac,wa,tle,re,ce,point,res
    cmd_cpp=["./main.out"]
    for run_i in range(run_number):
        run_result=decision(cmd=cmd_cpp,input_=testcase_inputs[run_i],
                            correct_output=correct_outputs[run_i])
        if run_result==0:
            res+=str(run_i)+":AC"
            if wa==0 and tle==0 and re==0:
                point+=allotment[run_i]
            ac+=1
        elif run_result==1:
            res+=str(run_i)+":WA"
            wa+=1
        elif run_result==2:
            res+=str(run_i)+":TLE"
            tle+=1
        elif run_result==3:
            res+=str(run_i)+":RE"
            re+=1
        res+="\n"
    return ac,wa,tle,re,ce,point,res


def run_ruby(object_file_name="",testcase_inputs=None,correct_outputs=None,allotment=None):
    ac,wa,tle,re,ce=[0]*5
    run_number=len(testcase_inputs)
    cmd_rb=["ruby",object_file_name]
    #結果をまとめて返す
    res=""
    point=0
    for run_i in range(run_number):
        run_result=decision(cmd=cmd_rb,input_=testcase_inputs[run_i],
                            correct_output=correct_outputs[run_i])        
        if run_result==0:
            res+=str(run_i)+":AC"
            if wa==0 and tle==0 and re==0:
                point+=allotment[run_i]
            ac+=1
        elif run_result==1:
            res+=str(run_i)+":WA"
            wa+=1
        elif run_result==2:
            res+=str(run_i)+":TLE"
            tle+=1
        elif run_result==3:
            res+=str(run_i)+":RE"
            re+=1
        res+="\n"
    return ac,wa,tle,re,ce,point,res


def run_python(object_file_name="",testcase_inputs=None,correct_outputs=None,allotment=None):
    ac,wa,tle,re,ce=[0]*5
    run_number=len(testcase_inputs)
    cmd_py=["python3",object_file_name]
    #結果をまとめて返す
    res=""
    point=0
    for run_i in range(run_number):
        run_result=decision(cmd=cmd_py,input_=testcase_inputs[run_i],
                            correct_output=correct_outputs[run_i])        
        if run_result==0:
            res+=str(run_i)+":AC"
            if wa==0 and tle==0 and re==0:
                point+=allotment[run_i]
            ac+=1
        elif run_result==1:
            res+=str(run_i)+":WA"
            wa+=1
        elif run_result==2:
            res+=str(run_i)+":TLE"
            tle+=1
        elif run_result==3:
            res+=str(run_i)+":RE"
            re+=1
        res+="\n"
    return ac,wa,tle,re,ce,point,res


def run(object_file_name="",testcase_inputs=None,correct_outputs=None,allotment=None):
    #テストケースと正解出力ファイルの数が同じでなければ実行させない
    if len(testcase_inputs)!=len(correct_outputs):
        print("Size Error:\nTestCase's size is ",len(testcase_inputs),"but",
            "CorrectOutPut's size is ",len(correct_outputs),".\n"
            +"Please check TestCase file and CorrectOutPut file.")
        return [-1]*5,""
    #拡張子だけ取り出したいから右から分割
    extension=object_file_name.rsplit(".",1)[1]
    res=""
    ac,wa,tle,re,ce=[0]*5
    #ジャッジする言語が増えればここに関数の追加
    if extension=="cpp":
        ac,wa,tle,re,ce,point,res=run_cpp(object_file_name,testcase_inputs,
                                correct_outputs,allotment)
    elif extension=="rb":
        ac,wa,tle,re,ce,point,res=run_ruby(object_file_name,testcase_inputs,
                                correct_outputs,allotment)
    elif extension=="py":
        ac,wa,tle,re,ce,point,res=run_python(object_file_name,testcase_inputs,
                                    correct_outputs,allotment)
    
    #最終結果を優先度順を考慮して分岐
    res+="Result:"
    if ce!=0:
        res+="CE"
    elif wa!=0:
        res+="WA"
    elif tle!=0:
        res+="TLE"
    elif re!=0:
        res+="RE"
    else:
        res+="AC"
    res+="\n"
    res+="Point:"+str(point)
    return ac,wa,tle,re,ce,res

if __name__=="__main__":
    print("Input decision name")
    decision_name=input()
    print("Input judged source name")
    file_name=input()
    print("Input point of judged file name")
    allotment_file_name=input()
    #各テストケースの得点は、別ファイルで保存
    allotment=file_accessor.read(file_name="./Allotment/"+str(allotment_file_name)+".txt",
                        separate_word="\n")
    if allotment==[]:
        print("FileError:\nAllotment file does not find")
        exit()
    allotment=list(map(int,allotment))
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
    ac,wa,tle,re,ce,res=run(object_file_name=file_name,testcase_inputs=testcases,
                        correct_outputs=correct_outputs,allotment=allotment)
    print(res)
    #print(ac,wa,tle,re,ce)

