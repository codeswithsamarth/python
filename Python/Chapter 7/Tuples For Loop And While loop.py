fruits = ('apple','banana','cheery')
for fruit in fruits:
    print(fruit)

fruits = ('apple','banana','cheery')
for i, frui in enumerate(fruits):
    print(f"{i},{frui}")

fruits = ('apple','banana','cheery')
for fruit in reversed(fruits):
    print(fruit)

fruits = ('apple','banana','cheery')
for i in range(len(fruits)):
    print(fruits[i])

fruits = ('apple','banana','cheery')
colors = ('red','yellow','pink')
for fruit, colors in zip(fruits,colors):
    print(f"{fruits}:{colors}")

fruits = (('apple','red'),('banana','yellow'),('cheery','pink'))
for fruit, colors in fruits:
        print(f"{fruit} is {colors}")

fruits = ('apple','banana')
more_fruits = ('cheery','date')
for fruit in fruits + more_fruits:
    print(fruit)

fruits = ('apple','banana')
for repatation in fruits * 2:
    print(repatation)

fruits = ('apple','banana')
for fruit in fruits[0:2]:
    print(fruit)

fruits = ('apple', 'banana', 'cheery')
for i in range(len(fruits)):
    print(fruits[i])

fruits = ('apple','banana','cheery','apple','banana','cheery')
for fruit in fruits:
    print(fruits.count(fruit))

fruits = ('banana','cheery','apple')
for fruit in sorted(fruits):
    print(fruit)

fruits = ('apple','banana','cheery')
for fruit in reversed(fruits):
    print(fruit)

fruits = ('apple','banana','cheery')
for fruit in fruits:
    if fruit == 'banana':
        print("Banana Found !")

numbers = (1,2,3,4,5,6)
print(max(numbers))
print(min(numbers))

numbers = (1,2,3,4,5,6)
print(any(x>3 for x in numbers))
print(all(x>0 for x in numbers))

numbers = (x**2 for x in range(5))
for num in numbers:
    print(num)

numbers = (1,2,3,4,5)
even_numbers = tuple(x for x in numbers if x % 2 == 0)
for num in even_numbers:
    print(num
          )
# Indexing
fruits = ('apple','banana','cheery')
for fruit in fruits:
    print(f"{fruit}:{fruits.index(fruit)}")



# While Loops

fruits = ('apple','banana','cheery')
i = 0
while i < len(fruits):
    print(fruits[i]
          )
    i+=1

fruits = ('apple','banana','cheery')
i = 0
while i < len(fruits):
    print(fruits[i]
          )
    i +=1

fruits = ('apple','banana','cheery')
i = 1
while i < 1:
    print(fruits[i])
    i +=1

fruits1 = ('apple','banana')
fruits2 = ('cheery','date')
i = 0
while i < len(fruits1 + fruits2):
    print((fruits1 + fruits2)[i])
    i+=1

fruits1 = ('apple','banana')
i = 0
while i < len(fruits1 * 2):
    print((fruits1 * 2)[i])
    i+=1

fruits = ('apple','banana','cheery')
i = 0
while i < len(fruits):
    if fruits[i] == 'banana':
        print("Found Banana")
        i+=1

fruits = ('apple','banana','cheery')
i = 0
while i < len(fruits):
    print("Hello")
    i+=1

