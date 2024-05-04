emojis = [
    ["🍇", "🏁", "🏍️", "🎃"],
    ["❤️", "🍁", "🥞", "🍩"], 
    ["🇺🇸", "🌎", "🌵", "👽"], 
    ["🚀", "🪐", "🦺", "📎"]
]


print("\n\n---- printing all items ----")
print("\nsimply print")
print(emojis)

print("\nloop through each row, print that row")
for row in emojis:
    print(row)


print("\nloop through each row, loop through each item in that row")
for row in emojis:
    for item in row:
        print(item, end=" ") # why end=" "? (try without)
    print() # why this? (try without)





# ---- looping through all items ----
print("\nlooping through using 'enhanced' loops")
for row in emojis:
    for item in row: # what type of data is 'row'? what type of data is 's'?
        print(item, end=" ") 
    print() 
    
    
print("\ncan we change items using 'enhanced' loops? (spoiler: no)")
for row in emojis:
    for item in row:
        item = 'xx'
print(emojis) # the list did not change


print("\nto change items, you must use indexed loops")
for r in range(len(emojis)): # what type of data is 'r'?
    for c in range(len(emojis[r])): # what type of data is students[r]?
        emojis[r][c] += '!'
print(emojis)


