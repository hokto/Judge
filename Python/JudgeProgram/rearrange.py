s=list(input())
output_s=list(input())
#0ならAC,1ならWA
if "".join(s) != "".join(output_s) and "".join(sorted(s)) == "".join(sorted(output_s)):
    print(0)
else:
    print(1)
