#解法としては、値段を連想配列のキーとして保存しておき、そのキーが存在するならば、
#そのキーの値が存在するならば値を2に、なければ、キーを追加して値を1にする。
#その後、連想配列のサイズから1引いたものの数列の和を考え、これにキーの値が２のものの個数を足せば
#それが答えとなる。

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
def array(size,n=1,init=nil) #nに配列の次元数、sizeに配列の大きさ、initに初期値を投げることでその配列を返す
  if n==1
    return Array.new(size){init}
  else
    return Array.new(n).map{Array.new(size){init}}
  end
end

n=gets.to_i
a=get_i
h={}
a.each do|num|
  if h[num]==nil
    h[num]=1
  else
    h[num]=2
  end
end
ans=0
h.each do|hash|
  ans+=hash[1]-1
end
m=h.size
puts (m-1)*m/2+ans
