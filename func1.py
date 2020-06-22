def aa():
    #多行文本
    """aaa
    aa
    """
    pass

print(aa.__doc__)

def aaa(a:str,b:str="b") ->str:
    print("Annotations:",aaa.__annotations__)
    print("Arguments:",a,b)
    return "a&b=" + a +b

a = aaa('aaaaaaaaaaaaaaaaaaaaa')
print("print(\'a\')=",a)