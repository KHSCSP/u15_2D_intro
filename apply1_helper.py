import random

def get_random(lst):
    position = random.randint(0, len(lst)-1)
    return lst[position]
      

emojis = ["🍇", "🏁", "🏍️", "🎃"]
print("here is a random item:", get_random(emojis))
