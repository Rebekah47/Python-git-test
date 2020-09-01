#tuple is immutable
#list is mutable

my_tuple = 'Ford', 'Escort', 1300, 'Red'
print(my_tuple)

my_tuple = 'Ford', 'Escort', 1300, 'Red'
print(my_tuple)

my_single_element_tuple = 'Ford', #needs comma at the end of single element list
print(my_single_element_tuple)

my_empty_tuple = () #creates and empty tuple
my_empty_tuple = tuple()

my_tuple_list = 1, "Steve", [1, 2, 3] 
print(my_tuple_list)

my_list_tuple = [1, "Steve", (2, 3, 4)] #cant edit tuple inside of list
print(my_list_tuple)

fruits = ("apple", "apple", "banana", "banana", "banana", "tangerine")
print(fruits.count("banana"))

print(fruits.index("tangerine"))

print(len(fruits))