#解法としては、現在の値段をciと表すと「もっとも値の小さいciを取り出してmから引くという操作を
#何回することができるか」という風に解釈できる。よって、PriorityQueueというアルゴリズムを用いて
#もっとも安い値段をqueueから取り出し、取り出した後にその値段にbiを加算し、またqueueに追加する
#という操作をmが0になるまで繰り返せばよく、PriorityQueueの計算量は、要素の追加、取り出し共に
#O(log N)なので、O(log N + M*log N)=O(M*log N)となり、間に合います。 

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

class PriorityQueue
  attr_accessor:queue,:n
  def initialize(n)
    @n=0
    @queue=array(2,n,10**9)
  end

  def push_q(x)
    i=@n
    @n+=1
    while i>0
      p_=(i-1)/2
      break if @queue[p_][0]<=x[0]
      @queue[i]=@queue[p_]
      i=p_
    end
    @queue[i]=x
  end

  def pop_q()
    min=@queue[0]
    @n-=1
    x=@queue[@n]
    i=0
    while i*2+1<@n
      l=i*2+1
      r=i*2+2
      l=r if r<@n and @queue[r][0]<@queue[l][0]
      break if @queue[l][0]>=x[0]
      @queue[i]=@queue[l]
      i=l 
    end
    @queue[i]=x
    return min
  end
end
n,m=get_i
pq=PriorityQueue.new(n)
a=get_i
b=get_i
n.times do|i|
  pq.push_q([a[i],b[i]])
end
ans=0
while true
  c=pq.pop_q()
  if m-c[0]>=0
    m-=c[0]
    c[0]+=c[1]
    pq.push_q(c) 
    ans+=1
  else
    break
  end
end
puts ans
