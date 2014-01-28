#Introducción a las listas

lista = ['d','d3','d4'];

lista.index('d3') to find an element in a list
lista.insert(posicion, elemento)
lista.insert(4, "d8")

my_list = [1,9,3,4,45]
for number in my_list:
  print number * 2

my_list.sort()

##Diccionarios en Python
d = {'key1': 1, 'key2':3}
print d['key2']

menu = {}
menu['Chicken Alfredo'] = 14.50
print menu['Chicken Alfredo']
menu['Chicken Alfredo'] = 14.50
menu['key2'] = 4.50
menu['key5'] = 10

###del dict_name[key_name]

###example of dictionary
inventory = {'gold': 500, 
'pouch': ['flint', 'twine', 'dagger'],
'backpack': ['bedroll', 'bread']
}
inventory['pouch'].sort()
inventory['pouch'].remove('flint')




