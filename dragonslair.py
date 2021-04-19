print("You enter the Dragons Lair!")
items = ["gold", "rubies", "emeralds", "an ancient sword", "a magic ring", "a sliver chalice"]

for item in items:
    print(item)
    
selectedItem = input("Which one do you want? ")

if selectedItem in items:
    SelectedItemSentence = "Very well, you have chosen " + selectedItem + "."
    print(SelectedItemSentence)
else:
    print("ROAR! I HAVEN'T GOT ONE OF THOSE!")
