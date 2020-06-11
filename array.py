array = [1,2,3,4,5]
print(array)

print(array[:])

array = array + [6,7,8,9,10,11,12,13]
print(array)

array.append(14)
print(array)

# array = [1,2,3]
# array = array + [4,5,6]
# array.append(4)
# array.append(5)
# array.append(6)
# array.append(4,5,6)
print(array[1:3])

print(len(array))

array1 = ['a','b','c']
array2 = [array,array1]

print(array2)

a,b = 0,1
print(a,b)
while a < 16:
    # print(a)
    print(a,end=",") # 控制是否换行
    a,b = b,a+b