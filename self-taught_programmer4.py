## Self-Taught Programmer Challenges for Chapter 4

# Challenge 1
def square():
    my_number = input("Give me a number: ")
    print(float(my_number) ** 2)

square()

# Challenge 2
def letters(string):
    print(str(string))

# Challenge 3
def overdone(x, y, z, a = 1, b = 2):
    pass

# Challenge 4
def first(x):
    return x / 2

def second(x):
    return x ** 2

print(second(first(6)))

# Challenge 5
def str_float(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")
