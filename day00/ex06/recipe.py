cookbook = {
    "sandwich" : {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time": 10
    },
    "cake" : {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time": 60
    },
    "salad" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time": 15
    }
}

def printMenu() :
    print ('''\
\
List of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit
\
''', end='')

def printRecipe(recipe) :
    if recipe in cookbook :
        print(f'''
\
Recipe for {recipe}:
    Ingredients list: {cookbook[recipe]['ingredients']}
    To be eaten for {cookbook[recipe]['meal']}.
    Takes {cookbook[recipe]['prep_time']} minutes of cooking.
\
''', end = '')
    else :
        print("\nrecipe don't exist")

def deleteRecipe(recipe) :
    if recipe in cookbook :
        del cookbook[recipe]
        print (f'\nrecipe {recipe} deleted')
    else :
        print(f"\nrecipe {recipe} don't exist")

def printCookbook() :
    print (f'\nnumber of Recipes {len(cookbook)}')
    for recipe in cookbook :
        print (f'    - {recipe}')

def addRecipe() :
    name = input('\n>>> Enter a name:\n')
    print('>>> Enter ingredients:')
    ingredients = []
    while True :
        ingredient = input()
        if ingredient and not ingredient.isspace() :
            ingredients.append(ingredient)
        else :
            break
    meal = input('>>> Enter a meal type:\n')
    while True :
        prep_time = input('>>> Enter a preparation time:\n')
        if not prep_time.isdigit() :
            print('pleas enter a number !!')
        else :
            break
    cookbook[name] = { "ingredients": ingredients, "meal" : meal, "prep_time" : int(prep_time) }
    print ('\nNew recipe has been added')

if __name__ == '__main__' :

    print('Welcome to the Python Cookbook !')
    printMenu()

    while True :
        print('\nPlease select an option:')
        option = input('>> ')
        if option == '1' :
            addRecipe()
        elif option == '2':
            deleteRecipe(input('\nPlease enter a recipe name to delet:\n>> '))
        elif option == '3':
            printRecipe(input('\nPlease enter a recipe name to get its details:\n>> '))
        elif option == '4':
            printCookbook()
        elif option == '5':
            print('EXITED')
            break
        else :
            print('\nSorry, this option does not exist.')
            printMenu()