## Self-Taught Programmer Challenges for Chapter 5

# Challenge 1
musicians = ["Kanye West", "Caamp", "Tyler the Creator", "Childish Gambino"]

# Challenge 2
my_homes = ("Kansas City", "St. Louis", "Lawrence")

# Challenge 3
about_me = {"age" : 24, "weight" : 190, "height" : 76}

# Challenge 4
for_me = {"height": 76, "favorite color": "blue", "favorite author": "Hemingway"}
def ask_me():
    m = input("Ask me about my height, favorite color, or favorite author: ")
    if(m == "height"):
        print(for_me["height"])
    elif(m == "favorite color"):
        print(for_me["favorite color"])
    elif(m == "favorite author"):
        print(for_me["favorite author"])
    else:
        print("That's not something I want to share")

ask_me()

# Challenge 5
music = {"Bobby Darin": "Splish Splash", "Frank Ocean": "Pyramids", "Kanye West": "Hey Mama", "Tyler the Creator":
         "Flower Boy"}
for songs in music:
    print(songs, " - ", music[songs])
