def get_i() #空白区切の入力を数値(整数)の配列で返す
  return gets.chomp.split(" ").map(&:to_i)
end
def get_f() #空白区切の入力を数値(実数)の配列で返す
  return gets.chomp.split(" ").map(&:to_f)
end
def get() #空白区切の入力を文字列の配列で返す
  return gets.chomp.split(" ")
end
def get_nsp() #入力されたものを一文字ずつに区切った文字列の配列で返す
  return gets.chomp.split("")
end
def yn_judge(bool,y="Yes",n="No") #boolに真偽を投げることで、trueならy、falseならnの値を出力する
  return bool ? y : n 
end
def array(size1,init=nil,size2=-1) #size2に二次元配列時の最初の要素数、size1に次の配列の大きさ、initに初期値を投げることでその配列を返す
  if size2==-1
    return Array.new(size1){init}
  else
    return Array.new(size2){Array.new(size1){init}}
  end
end

H,W=get_i
c=array(H)
H.times do|i|
    c[i]=get_nsp
end
s=nil
g=nil
H.times do|i|
    W.times do|j|
      if c[i][j]=="s"
        s=[j,i]
      elsif c[i][j]=="g"
        g=[j,i]
      end
    end
end
dp=array(W,0,H)
Dir_=[[1,0],[0,1]]
dp[s[1]][s[0]]=1
MOD=10**9+7
H.times do|i|
    W.times do|j|
        Dir_.each do|x,y| 
            next if c[i][j]=="#"
            dp[i][j]+=dp[i-y][j-x] if (i-y).between?(0,H-1) and (j-x).between?(0,W-1)
            dp[i][j]%=MOD
        end
    end
end
if dp[g[1]][g[0]].zero?
    puts "-1"
else
    puts dp[g[1]][g[0]]
end
