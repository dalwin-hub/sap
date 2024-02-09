fruits=['apple','mango','grape']
fruits1=['banana']
fruits1[0]='orange'
print(fruits)
print(fruits[1])
print(fruits[0:1])         #slice
print(len(fruits))         #length
print(fruits+fruits1)      #concat
print(fruits1)             #replace
fruits.reverse()
print(fruits)              #reverse

a=[1,2,3,4,5]
b=[21,22,23,24,25]
a.extend(b)
a.append(29)
print(a)

