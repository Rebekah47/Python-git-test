meals = ['yoghurt', 'roll', 'steak']
my_first_empty_dictionary = {} #create empty dictionary
my_second_empty_dictionary = dict()

meals = {"breakfast": "yogurt", "lunch": "roll", "dinner": "steak"} #creates keys for your elements
print(meals)

silly_thing = {1: "2", 2:"3", 4: False}
print(silly_thing)
print(meals["breakfast"])

meals["dinner"] = "pasta" #modifies and element 
print(meals)

del(meals["breakfast"]) #deletes key (and element) from dictionary
print(meals)

meals["Elevenses"] = "cake"
print(meals)

print(list(meals)) #lists the keys of the dictionary
print(meals.keys()) #lists the keys of the dictionary *slightly different format than above
print(meals.values()) #list elements

countries = {
    "UK":{
        "Capital": "London", "Population": 1000
    },
    "Germany": {
        "Capital": "Berlin",
        "Population": 5
    }
}
print(countries)
print(countries["Germany"]["Population"])

