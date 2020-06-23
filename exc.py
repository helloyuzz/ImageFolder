# while True:
#     try:
#         a = int(input('number:'))
#         print('a = {0}'.format(a))
#         break;
#     except ValueError:
#         print('type error:',ValueError)


print('a')


class B(Exception):
        pass

class C(B):
    pass

class D(C):
    pass

for item in [B,C,D]:
    try:
        raise item()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')