n, m = map(int, input().split())
result = 0

while True : 
    target = (n//m)*m
    rsult += (n-target)
    n = target
    if n<k : 
        break
    result += 1
    n//=m
    
result += (n-1)
print(result)


# n, m = map(int, input().split())
# result = 0d

# while n >= m : 
#     while n % m != 0 : 
#         n-=1
#         result+=1
#     n //= m
#     result += 1
    
# while n>1 : 
#     n-=1
#     result += 1
    
# print(result) 