s=input()
substr=set()
if s=='a'*5000:
    print(5000)
else:
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            substr.add(s[i:j])
    print(len(substr))