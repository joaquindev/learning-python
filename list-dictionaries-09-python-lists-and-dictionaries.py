zoo_animals = ["pangolin", "cassowary", "sloth", "dog"];

if len(zoo_animals) > 3: 
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "elephant"

####Late arrivals & List Length
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("bag")
suitcase.append("phone")
suitcase.append("table")



list_length = len(suitcase)# Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

####List Slicing
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first =    suitcase[0:2]# The first two items
middle =   suitcase[2:4]# Third and fourth items
last =     suitcase[4:6]# The last two items

####Maintaining Order
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation

####For One and all
my_list = [1,9,3,8,5,7]

for number in my_list:
    print number * 2
    

####More with for
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number ** 2)
    
square_list.sort()


print square_list

####This Next part is key
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

print residents['Sloth']
print residents['Burmese Python']

####New Entries
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

menu['key1'] = 58
menu['key2'] = 22
menu['key3'] = 55





print "There are " + str(len(menu)) + " items on the menu."
print menu

####Changing your mind
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = "Anything other"



print zoo_animals


####It's dangerous to go alone. Take this
inventory = {'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Here the dictionary access expression takes the place of a list name 

inventory['pocket'] = ['seashell','strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
nventory['gold'] += 50
