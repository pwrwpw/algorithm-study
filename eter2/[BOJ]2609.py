n, m = input().split()
n = int(n)
m = int(m)

def gcd(m,n):
    if m < n:
        m, n = n, m
    
    if n == 0:
        return m
        
    if m % n == 0:
        return n
        
    return gcd(n, m % n)
	    
print(gcd(n, m))
print(int(n*m / gcd(n,m)))