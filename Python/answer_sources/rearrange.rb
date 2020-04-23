S=gets.chomp.split("")
if S.size==2
    puts [S[1],S[0]].join("")
end
puts S.shuffle.join("")
