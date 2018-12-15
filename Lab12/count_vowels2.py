s=str(input())
ss=['a','e','i','o','u','A','E','I','O','U']
ans=0
for i in s:
    if i in ss:
        ans+=1
print(ans)