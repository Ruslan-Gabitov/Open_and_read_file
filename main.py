def get_cook_book(file):
    cook_book = {}
    with open (file) as recipes:
        while True:
            item = recipes.readline().strip()
            if item == '':
                return cook_book
            ingridients = []
            cook_book[item] = ingridients
            number = recipes.readline().strip()
            if number.isdigit():
                for i in range(int(number)):
                    ingredient_name, quantity, measure = recipes.readline().strip().split(' | ')
                    ingridients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            recipes.readline().strip()


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    cook_book = get_cook_book("recipes.txt") 
    for dish in cook_book:
        if dish in dishes:
            for ingredient in cook_book[dish]:
                ingredients[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
    return ingredients            


def get_sorted_files(files):
    count = {}
    sorted_file = {}
    for file in files:
        with open (file) as item:
            number_of_rows = sum(1 for line in item if line.strip())
            count[number_of_rows] = file
    for lines in sorted(count):
        sorted_file[count[lines]] = lines
    return sorted_file


def get_merged_file(files):
    text = ''
    for file, lines in files.items():
        with open (file) as item:
            text = item.read()
        with open('merged_file.txt', 'a', encoding='utf=8') as merged_file:
            merged_file.write(f'{file}\nСтрок: {lines}\n{text}\n')
    

if __name__ == "__main__":
    get_merged_file(get_sorted_files(['1.txt', '2.txt', '3.txt']))
    print(get_cook_book('recipes.txt'))
    print()
    print()
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))