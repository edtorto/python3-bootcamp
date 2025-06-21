programming_dictionary = {
    "Bug": "An error in a program that prevents a program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# creating an empty dictionary
empty_dictionary = {}

# wiping an existing empty_dictionary
# programming_dictionary = {}
# print(programming_dictionary) # type: ignore

# Edit item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer" 

# Loop through a dictionary
for key in programming_dictionary:
    # print keys
    print(key)
    print(programming_dictionary[key])

# Nested dictionaries
# A dictionary in a dictionary
travel_log = { # type: ignore
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

def add_new_contry(country: str, visits: int, list_of_cities:list): # type: ignore
    # Adding new data to a nested dictionary
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = list_of_cities,
    new_country["total_visits"] =  visits,
    travel_log.append(new_country) # type: ignore
    
# Accessing nested dictionary items
print(travel_log["France"]["cities_visited"][0])  # type: ignore # Output: Paris
print(travel_log["Germany"]["total_visits"])  # type: ignore # Output: 5

# Adding new data to a nested dictionary
add_new_contry("Italy", 3, ["Rome", "Venice", "Florence"])

# Adding a new city to an existing country
travel_log["France"]["cities_visited"].append("Nice")  # type: ignore

# Nesting dictionaries in a list
travel_log_list = [ # type: ignore
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },              
    {
        "country": "Italy",
        "cities_visited": ["Rome", "Venice", "Florence"],
        "total_visits": 3,
    },
]

# Looping through a list of dictionaries
for country in travel_log_list: # type: ignore
    print(f"Country: {country['country']}")  # type: ignore
    print(f"Cities visited: {', '.join(country['cities_visited'])}")  # type: ignore
    print(f"Total visits: {country['total_visits']}")  # type: ignore
    print()  # Print a newline for better readability

