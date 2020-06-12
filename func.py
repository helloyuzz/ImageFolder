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

def ask_ok(prompt,times=4,tip="try"):
    while True:
        ok = input(prompt)
        if ok in ('y','o'):
            return True
        if ok in ('n','f'):
            return False
        times = times - 1

        if times < 0:
            raise ValueError('invalid value')
        print(tip)

ask_ok('aa')
ask_ok('ask_ok',3)
ask_ok('aaa',3,"aaaaaaaaaaaaaaaaaa")