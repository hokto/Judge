require "open3"

status=Open3.capture3("g++ sample.cpp -o sample.out")
p status
