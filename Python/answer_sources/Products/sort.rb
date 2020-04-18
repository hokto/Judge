#これは、愚直にやるとすれば、バブルソートを構築して操作後の数列を比較すればいいが、
#今回は、N<100_000なので間に合わない。そこで、BinaryIndexeedTreeを用いて、バブルソートの転倒数
#を求めることを使って、二つの数列における転倒数を求め、これの差を求めれば良い。

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

class BinaryIndexeedTree
  attr_accessor:node,:n
  def initialize(n)
    @n=n
    @node=array(@n+1,1,0)
  end

  def add(i,x)
    while i<=@n
      @node[i]+=x
      i+=i&-i
    end
  end

  def getSum(i)
    s=0
    while i>0
      s+=@node[i]
      i-=i&-i
    end
    return s
  end
end

n=gets.to_i
bit1=BinaryIndexeedTree.new(n)
bit2=BinaryIndexeedTree.new(n)
v_fall=0
p_fall=0
v=get_i
p=get_i
n.times do|i|
  v_fall+=i-bit1.getSum(v[i])
  bit1.add(v[i],1)
  p_fall+=i-bit2.getSum(p[i])
  bit2.add(p[i],1)
end
puts v_fall-p_fall
