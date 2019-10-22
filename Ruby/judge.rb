require"open3"
require"fileutils"

def Judge(targetNumber,file)
fileName=file.split(".")
errorMessage=""
judgeResult=[]
if(fileName[1]=="cpp")
system("g++ -o #{fileName[0]}.exe #{fileName[0]}.cpp 2> Error.txt")
File.open("Error.txt","r") do|file|
	 errorMessage=file.read
end
FileUtils.rm("Error.txt")
end
if(errorMessage !="")
	puts "Result:CE"
	puts errorMessage
    judgeResult[0]=[]
    judgeResult[0][0],judgeResult[0][1]="CE",errorMesssage
else
	tleList=[]
    File.open("../TestCase/#{targetNumber}testcase.txt",mode="rt"){|f|
		idx=0
		f.each_line(rs=""){|line|
			input=line.chomp(rs="")
			start=Time.now
                        if(fileName[1]=="cpp")
                          Open3.capture3("#{fileName[0]}.exe >> output.txt",:stdin_data=>"#{input}\n")
                        elsif(fileName[1]=="py") 
                          Open3.capture3("python3 #{fileName[0]}.py >> output.txt",:stdin_data=>"#{input}\n")
                        elsif(fileName[1]=="rb")
                          Open3.capture3("ruby #{fileName[0]}.rb >> output.txt",:stdin_data=>"#{input}\n")
                        end
			finish=Time.now
			if(finish-start>2.0)
				tleList.push(idx)
			end
			File.open("output.txt",mode="a"){|outF|
				outF.write("\n")
			}
			idx+=1
		}
	}
	result=[]
    File.open("../Result/#{targetNumber}result.txt",mode="rt"){|answerF|
		answerF.each_line(rs=""){|answerLine|
			result.push(answerLine.chomp(rs=""))
		}
	}
	resultFlag=0
	File.open("output.txt", mode="rt") {|resultF|
		idx=0
		resultF.each_line(rs=""){|resultLine|
			playerAns=resultLine.chomp(rs="")
			if (tleList !=[] and tleList[0]==idx)
				puts "#{idx+1}:TLE"
				resultFlag=1
				tleList.shift()
                judgeResult.push("TLE")
			elsif(result[idx]!=playerAns)
				puts "#{idx+1}:WA"
				resultFlag=2
                judgeResult.push("WA")
			else
				puts "#{idx+1}:AC"
                judgeResult.push("AC")
			end
			idx+=1
		}
	}
	case resultFlag
		when 0 then
			puts "Result:AC"
            judgeResult.push("AC")
		when 1 then
			puts "Result:TLE"
            judgeResult.push("TLE")
		when 2 then
			puts "Result:WA"
            judgeResult.push("WA")
	end
	FileUtils.rm("output.txt")
end
return judgeResult
end
