a = 123
b = 'abc'

# use 'f' or 'F' to format
print(f"format:{a}-{b}")

a = 123_456
b = 126_567

c = a / (a + b)
print('{:-9}----{:2.2%}'.format(a,c))

import math
print(f'math.pi = {math.pi:.13f}.')

aa = {'a':1,'b':2,'c':3}
for key,value in aa.items():
    # print(f'key={key:16},value={value:13}'.format(key,value))
    print(f'key={key:16},value={value:13}')

aa = 'eels'
print(f'aa = {aa}')
print(f'aa!r = {aa!r}')

aa = 'aa-({})<-->({})'
print(aa.format('knight','Ni'))

print('{{0}}={0}，{{1}}={1}'.format('a','b'))

print('{{1}}={1}，{{0}}={0}'.format('a','b'))

print('{{key}}={{value}} like:\"{key}={value}\"'.format(key='the key',value='the value'))

table ={'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678} #{'a':1,'b':2,'c':3}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))#'b=:{0[b]:d};a=:{0[a]:d};c={0[c]:d}'.format(aa))

aa = {'a':1,'b':2,'c':3}
print('b={0[b]:d},a={0[a]:d},c={0[c]:d}'.format(aa))

import math

print('The value of pi is approximately %5.13f.' % math.pi)
print('math.pi=%5.13f.' %math.pi)