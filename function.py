s=input("Enter the string:").lower()
out={}
for i in s:
    out[i]=s.count(i)
sort=sorted(out.items(),key=lambda x: x[1],reverse=True)
for i in sort:
    print(f"{i[0]}={i[1]}")
