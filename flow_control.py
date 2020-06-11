## if
# x = int(input("input x:"))
x = 123
if x < 123: 
    print("less 123")
elif x == 123:
    print("equals 123")
else:
    print("than 123")

## while
a = 123
while a >=0:
    print(a)
    a -= 1

## for
array = ['aa','bb','cc']
for item in array:
    print(item,len(item),item.capitalize())

length = range(len(array))
for i in length:
    print(array[i])

print("for loop in range()")

## FAQ
array = [{'aa':1},{'bb':2}]
for key in array:
    # print(key.items()) 
    for value in key.items():
        print(key,value)

## range()
for i in range(5):
    print(i)

print(len(range(1,61)))

i = range(1,100,3)
for n in i:
    print(n)

## for and else
## like finally{...}
for n in range(3):
    if n % 2 ==0:
        print(n,'偶数')
else:
        print(n,"基数")