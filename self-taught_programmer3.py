## Self-Taught Programmer Challenges for Chapter 3

# Challenge 1
print("I am the first string,")
print("I come second,")
print("I am third and the last string to be printed")

# Challenge 2
def comp(x):
    if(x < 10):
        print("I am less than 10")
    else:
        print("I am 10 or greater than 10")

# Challenge 3
def three_things(x):
    if (x <= 10):
        print("I am little")
    elif(x > 10 and x <= 25):
        print ("I am not little or big")
    else:
        print("I am big!")

# Challenge 4
def whats_left(x, y):
    print( x % y)

# Challenge 5
def what_you_get(x, y):
    print(x // y)

# Challenge 6
def how_old():
    age = input("How old are you? ")
    print("I am " + age + " years old!")

how_old()