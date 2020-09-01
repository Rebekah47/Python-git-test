fruits = ['apple', 'banana', 'grape', 'orange']

print(fruits)
print(fruits[1])
print(fruits[-1])
fruits[1] = "mango"
print(fruits)

my_list = [] #creates and emtpy list
my_list = list() #creates and emtpy list

num_items = len(fruits) #len() gives number of items in this list
print(num_items) 

fruits.append('pear') #adds item to list
print(fruits)

fruits.pop() #removes last element on list
print(fruits)

fruits.remove('apple') #removes chosen element from list
print(fruits)

fruits_and_numbers = ['apple', 1, 'grape', 2] #can inclsude elemetns of differetn types
print(fruits_and_numbers)

nested_list = [1, 2, 3, 4, [5, 6, 7]]
print(nested_list)
print(nested_list[4][1])

