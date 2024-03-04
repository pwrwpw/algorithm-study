
def gcd(value_1,value_2):
    if value_1 < value_2:
        value_1,value_2 = value_2,value_1

    while value_2 != 0:
        value_1, value_2 = value_2, value_1 % value_2

    return value_1

def lcm(value_1,value2,value3):
    return value_1 * value2 // value3

a,b = map(int,input().split())
gcd_value = gcd(a,b)
print(gcd_value)
print(lcm(a,b,gcd_value))