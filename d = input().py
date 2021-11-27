def check(s):
    result = 0
    for a in s:
        if "(" in a:
            result +=1
        elif ")" in a:
            result -= 1
 
        if result < 0:
            return"NO"
    if result > 0:
        return"NO"
    return "YES"
 
print(check(input()))