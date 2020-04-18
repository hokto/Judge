#解法としては、区間内の総和を求めることが必要なのでRangeSumQuery(RSQ)を用いて考える
#しかし、今回は、値の更新が範囲的に行われるため、セグメント木でRSQを実装すると、N<10**5
#までは間に合わない。そこで、遅延伝搬セグメント木を用いて範囲的な更新を可能にし、最初に
#指定された範囲の総和を出力し、その後、その範囲の更新を行えば良い。

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

class LazySegTree
  attr_accessor:node,:lazy,:n
  def initialize(n)
    @n=1
    @n*=2 while @n<n
    @node=array(2*@n-1,1,0)
    @lazy=array(2*@n-1,1,0)
  end

  def lazy_eval(i,l,r)
    unless lazy[i].zero?
      @node[i]+=@lazy[i]
      if r-l>1
        @lazy[i*2+1]+=@lazy[i]/2
        @lazy[i*2+2]+=@lazy[i]/2
      end
      @lazy[i]=0
    end
  end

  def add(s,t,x,i,l,r)
    lazy_eval(i,l,r)
    return if r<=s or t<=l
    if s<=l and r<=t
      @lazy[i]=(r-l)*x
      lazy_eval(i,l,r)
    else
      mid=(l+r)/2
      add(s,t,x,i*2+1,l,mid)
      add(s,t,x,i*2+2,mid,r)
      @node[i]=@node[i*2+1]+@node[i*2+2]
    end 
  end

  def getSum(s,t,i,l,r)
    return 0 if r<=s or t<=l
    lazy_eval(i,l,r)
    return @node[i] if s<=l and r<=t
    mid=(l+r)/2
    leaf_l=getSum(s,t,i*2+1,l,mid)
    leaf_r=getSum(s,t,i*2+2,mid,r)
    return leaf_l+leaf_r
  end
end
n,m=get_i
a=get_i
lst=LazySegTree.new(n)
n.times do|i|
  lst.add(i,i+1,a[i],0,0,lst.n)
end
m.times do
  l,r,x=get_i
  l-=1
  r-=1
  puts lst.getSum(l,r+1,0,0,lst.n)
  lst.add(l,r+1,x,0,0,lst.n)
end

