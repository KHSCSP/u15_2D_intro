# ---- try this! ----
# create a 2D list with 3 rows and 4 columns
# print your list
# print your list using enhanced loops
# print your list using indexed loops

stuff = [
    ["🍇", "🏁", "🏍️", "🎃"],
    ["❤️", "🍁", "🥞", "🍩"], 
    ["🇺🇸", "🌎", "🌵", "👽"], 
    ["🚀", "🪐", "🦺", "📎"]
]
print("\nprinting 'stuff'")
print(stuff)

print("\nprinting using enhanced loops")
for row in stuff:
    for item in row:
        print(item, end=" ")
    print()

print("\nprinting using indexed loops")
for r in range(len(stuff)):
    for c in range(len(stuff[r])):
        print(stuff[r][c], end=" ")
    print()



