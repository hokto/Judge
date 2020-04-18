n=Random.new.rand(2..100)
puts "N:#{n}"
v=Array.new(n){|i| i+1}
v.shuffle!
puts v.join(" ")
k=Random.new.rand(0..100*2)
cnt=0
(n-1).times do|i|
  (n-1).downto(i+1) do|j|
    if v[j]<v[j-1]
      v[j],v[j-1]=v[j-1],v[j]
      cnt+=1
      if cnt>=k
        break
      end
    end
  end
  if cnt>=k
    break
  end
end
puts "Count:#{cnt}"
puts v.join(" ")
