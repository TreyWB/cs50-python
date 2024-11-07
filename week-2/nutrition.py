import sys

def main():
    item = input("Item: ")

    cal = get_info(item.lower())
   
    if cal == None:
        sys.exit()
    
    print("Calories:", cal)

def get_info(item):
    fruits = [
        {"name": "apple", "Calories": "130"},
        {"name": "avocado", "Calories": "50"},
        {"name": "banana", "Calories": "110"},
        {"name": "cantaloupe", "Calories": "50"},
        {"name": "grapefruit", "Calories": "60"},
        {"name": "grapes", "Calories": "90"},
        {"name": "honeydew melon", "Calories": "50"},
        {"name": "kiwifruit", "Calories": "90"},
        {"name": "lemon", "Calories": "15"},
        {"name": "lime", "Calories": "20"},
        {"name": "nectarine", "Calories": "60"},
        {"name": "orange", "Calories": "80"},
        {"name": "peach", "Calories": "60"},
        {"name": "pear", "Calories": "100"},
        {"name": "pineapple", "Calories": "50"},
        {"name": "plums", "Calories": "70"},
        {"name": "strawberries", "Calories": "50"},
        {"name": "sweet cherries", "Calories": "100"},
        {"name": "tangerine", "Calories": "50"},
        {"name": "watermelon", "Calories": "80"}
        ]

    i = 0

    for fruit in fruits:
        if fruit["name"] == item:
            cal = fruits[i]["Calories"]
            return cal
        
        i += 1

main()