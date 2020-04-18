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

N,M,K=get_i
A=get_i.sort
ng_temp=get_i
ng={}
ng_temp.each do|ng_|
    ng[ng_]=1
end
dp=array(N+1,false)
dp[0]=true
A.each do|a|
    dp[a]=true if ng[a].nil?
end
1.upto(N) do|i|
    A.each do|a|
       break if i*a>N
       dp[i*a]=dp[i] if dp[i] and ng[dp[i]].nil?
    end
end
puts yn_judge(dp[N])
