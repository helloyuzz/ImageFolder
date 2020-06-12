i = 5
def a(arg = i):
    print(arg)
i = 6
a()
a(6)

## 多次调用之间，默认共享值地址，非常重要的不同！！！
def aa(a,L=[]):
    L.append(a)
    return L

print(aa(1))
print(aa(2))
print(aa(3))

## 多次调用之间不共享值地址，采用None表示
def aa1(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(aa1(1))
print(aa1(2))
print(aa1(3))

## key - value参数
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

print("aa",end="")
print("aa")

## 动态参数和
def aa_1(aa,*dd,**ee):
    print("aa=",aa)
    for argu in dd:
        print("*dd=",argu)
    print("-"*40)

    for item in ee:
        print("*ee=",item,"=",ee[item])
    print("-"*40)

aa_1("aa")
aa_1("aa","bb","cc")
aa_1("aa","bb","cc",key="key1",item="value")