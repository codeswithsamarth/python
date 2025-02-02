# Dictionary is a collection of keys-value pairs.

marks = {
    "Harry":100,
    "Rohit":91,
    "Sanket":98,
     0:"Harry"
}

print(marks["Sanket"])

print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"Harry":99,"Harshit":97}))

print(marks.get("Harry"))

final_marks = marks.copy()
print(final_marks)

clear_marks = marks.clear()
print(marks)

keys = ['a','b','c']
my_dict = dict.fromkeys(keys,0)
print(my_dict)

vote = ["BJP","BJP","BJP","BJP","Congress","Congress","Congress","AAP","AAP","NOTA"] * 500

vote_count = dict.fromkeys(list(vote),0)
for count in vote:
    vote_count[count] += 1
    print(vote_count)

winner = max(vote_count,key=vote_count.get)
print(winner)
