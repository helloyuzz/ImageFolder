from collections import deque

a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
aa = deque([1,2,3,4,5,6,7,8,9,10,12,13])

print(a.count(1))
print(a.index(3))
a.pop()
print(a)

aa.popleft()
print(aa)

aa = [n ** 2 for n in range(63)]
print(aa)

aa = list(map(lambda n:n**2,range(63)))
print(aa)

bb = dict([("aa",1),("bb",2)])
print(bb)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

for idx,value in enumerate(['a','b','c']):
    print(idx,value)

