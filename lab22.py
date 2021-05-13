

##
fruitbowl = ["apple", "tomatoe", "bean"]

for fruit in fruitbowl:
    print(fruit)

fruitfile = open("fruitfile.txt","a")
for fruit in fruitbowl:
    print(fruit, file=fruitfile)

fruitfile.close()

fruitbowl = ["cherry", "orange", "carrot"]

for fruit in fruitbowl:
    print(fruit)

fruitfile = open("fruitfile.txt","a")
for fruit in fruitbowl:
    print(fruit, file=fruitfile)

fruitfile.close()
