import random

# given a 2D list, return a random item from that list
def get_random(lst):
    row = random.randint(0, len(lst)-1)
    col = random.randint(0, len(lst[0])-1)
    return lst[row][col]



emojis = [
    ["🍇", "🏁", "🏍️", "🎃"],
    ["❤️", "🍁", "🥞", "🍩"], 
    ["🇺🇸", "🌎", "🌵", "👽"], 
    ["🚀", "🪐", "🦺", "📎"]
]


print("here is a random item:", get_random(emojis))