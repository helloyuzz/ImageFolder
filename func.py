## invoke function
def aa(n):
    a,b = 0,1
    while a < n:
        print(a,end=",")
        a,b = b,a+b
    print()

aa(3)


## result
def aa1(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result

get_aa1 = aa1(3)

print(get_aa1)