# nums = int(input("Enter Your Number"))
# factorial = 1
# for i in range(1, nums + 1):
#     factorial *= i
#     print(factorial)
#
#
# n = int(input("Enter The Number"))
# a,b = 0,1
# for _ in range(n):
#     print(a,end=" ")
#     a,b = b,a+b

# number = int(input("\nEnter Number To check:"))
# if number >= 1:
#     for i in range(2,int(number**0.5),+1):
#         if number % i == 0:
#             print("The Number Is Not a Prime Number")
#             break
#         else:
#             print("It is a Prime Number")
#             break
#

number = range(100)
for num in [n**2 for n in number]:
    print(num)


number = range(100)
for even in [x for x in range(100) if x%2 == 0]:
    print("The Number Is even",even)

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")

for l in range(1,11):
    print(f"{5} into {l} is = {5*l}")


# str1 = input("Enter The First Text:")
# str2 = input("Enter The Second Text:")
# if sorted(str1) == sorted(str2):
#     print("The String are anagrams")
# else:
#     print("The String are Not anagrams")


# text = input("Enter The Text:")
# count = dict.fromkeys(text,0)
# for char in text:
#     count[char] += 1
#     print(count)

text = input("Enter The Text:")
result = set(text)
print(sorted(result))

result2 = "".join(dict.fromkeys(text))
print(result2)

text2 = input("Enter Text To Reverse:")
reverse = text2[::-1]
print(reverse)

