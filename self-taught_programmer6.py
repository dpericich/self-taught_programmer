## Self-Taught Programmer Challenges for Chapter 6

# Challenge 1
author = "Camus"
for char in author:
    print(char)

# Challenge 2
m1 = input("Enter an item ")
m2 = input("Enter a person ")
message = "Yesterday I wrote a {}. I sent it too {}!".format(m1, m2)
print(message)

# Challenge 3
stuff = "aldous Huxley was born in 1894."
print(stuff.capitalize())

# Challenge 4
questions = "Where now? Who now? When now?"
print(questions.split("?"))

# Challenge 5
rhyme = ["The", "fox", "jumped", "over", "the", "fence", "."]
rhyme = " ".join(rhyme)
rhyme = rhyme[0: -2] + "."
print(rhyme)

# Challenge 6
scream = "A screaming comes across the sky."
scream = scream.replace("s" or "S", "$")
print(scream)

# Challenge 7
author2 = "Hemingway"
print(author2.index("m"))

# Challenge 9
word = "three "
print(word * 3)
print(word + word + word)

# Challenge 10
sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
print(sentence[34:])