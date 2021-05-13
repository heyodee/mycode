fruitbowl = ["apple", "tomato", "bean"] 

for fruit in fruitbowl:
    print(fruit) 

# try replacing "a" with "w" -----+
#                                 v
fruitfile = open("fruitfile.txt","a")
for fruit in fruitbowl: 
    print(fruit, file=fruitfile)

fruitfile.close()
 
fruitbowl = ["cherry", "orange", "carrot"]
 
for fruit in fruitbowl: 
    print(fruit) 

# try replacing "a" with "w" -----+
#                                 v
fruitfile = open("fruitfile.txt","a") 
for fruit in fruitbowl:
    print(fruit, file=fruitfile) 
 
fruitfile.close()   