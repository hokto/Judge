#この問題は、各店員の関係をグラフで考えればよい。店員iと店員jが親族同士であれば、２つを
#連結し、このグラフの数を求めることで親族の数が求まり、各グラフの節点の数の最大値をとればこれが
#親族の最大の人数となる。しかし、愚直にグラフを作成しても間に合わないため、高速に節点同士が
#連結しているかどうか判定できるUnionFindTreeを用いることで求められる。


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

class UnionFindTree
  attr_accessor:par,:rank,:size
  def initialize(n)
    @par=Array.new(n){|i| i}
    @rank=array(n,1,0)
    @size=array(n,1,1)
  end

  def find(x)
    return x if @par[x]==x
    @par[x]=find(@par[x])
    return @par[x]
  end

  def union(x,y)
    x=find(x)
    y=find(y)
    return if x==y
    if @rank[x]<@rank[y]
      @par[x]=y
      @size[y]+=@size[x]
    else
      @par[y]=x
      @size[x]+=@size[y]
      @rank[x]+=1 if @rank[x]==@rank[y]
    end
  end

  def same?(x,y)
    return find(x)==find(y)
  end

  def size(x)
    return @size[find(@par[x])]
  end
end

n,m=get_i
uft=UnionFindTree.new(n)
m.times do|i|
  x,y=get_i
  x-=1
  y-=1
  uft.union(x,y)
end

ans=[]
relatives=[]
n.times do|i|
  relatives.push(uft.find(i))
end
relatives.uniq!
ans.push(relatives.size)
max=0
relatives.each do|num|
  val=uft.size(num)
  max=val if max<val
end
ans.push(max)
puts ans.join(" ")
