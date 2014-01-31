names = ["Adam","Alex","Mariah","Martine","Columbus"]

for item in names: 
     print item

webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]

#Control flow and looping
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in a:
    if item % 2 == 0:
         print item

#List + Functions
#Functions can also take lists as inputs and perform various operations on those lists

def fizz_count(x):
  count = 0
  for item in x: 
    if item == 'fizz':
      count += 1;
  return count;

#String Looping
for letter in "Codeacademy":
  print letter

#Empty lines to make the output pretty
print
print

word = "Programming is fun!"
for letter in word:
    if letter == "i":
      print letter

#Your Own score
print "YOUR OWN SCORE"
print
prices = { "banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

stock = { "banana": 6, "apple": 0, "orange": 32, "pear": 15}

for item in prices: 
    print item;
    print "price: " + str(prices[item]);
    print "stock: " + str(stock[item]);

print

#Something of Value
print

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
    
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0;
for item in prices:
    total += prices[item]*stock[item];

print total

#Shopping at the Market. Einkaufen auf dem Markt
print
print "Einkaufen auf dem Markt"
groceries = ["banana", "orange", "apple"]
stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total=0
    for items in food:
        total+= prices[items]
    return total 

print compute_bill(["apple"]);

#Stocking OUT
print
print "Stocking Out"

shopping_list = ["banana", "orange", "apple"]

stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total=0
    for items in food:
        total+= prices[items]
    return total 


def compute_bill(shopping_list):
    total=0
    for items in shopping_list:
        if stock[items] != 0: 
            total+= prices[items];
            stock[items] -= 1;
    return total 


