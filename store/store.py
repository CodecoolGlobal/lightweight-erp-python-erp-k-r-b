""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    while True:
        options = ["Show table",
                   "Add",
                   "Remove",
                   "Update",
                   "How many different kinds of game are available of each manufacturer?",
                   "What is the average amount of games in stock of a given manufacturer?"]
        ui.print_menu("Stores", options, "Back to main menu")

        table = data_manager.get_table_from_file("store/games.csv")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        try:
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs(["Please provide ID to remove: "], "")
                remove(table, id_[0])
            elif option == "4":
                id_ = ui.get_inputs(["Please give me an ID to update: "], "")
                update(table, id_[0],)
            elif option == "5":
                get_counts_by_manufacturers(table)
            elif option == "6":
                manufacturer = ui.get_inputs(["Please Give me the Manufacturer Name: "], "")
                get_average_by_manufacturer(table, manufacturer)
            elif option == "0":
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    table = data_manager.get_table_from_file("store/games.csv")
    title_list = ["ID", "Title", "Manufacturer", "Price", "Stock"]
    ui.print_table(table, title_list)


def add(table):
    list_labels = ["Title",
                   "Manufacturer",
                   "Price",
                   "Stock"]
    new_id = common.generate_random()
    new_data = ui.get_inputs(list_labels, "")
    new_data.insert(0, new_id)
    table = common.add_line_to_file("store/games.csv", new_data)
    return table


def remove(table, id_):
    for i in range(len(table)):

        if table[i][0] == id_:
            del table[i]
            break
    data_manager.write_table_to_file("store/games.csv", table)
    return table


def update(table, id_):
    for sublist in table:
        if id_[0] in sublist:  # look for the ID in sublist
            inputs = ui.get_inputs(["ID", "Title", "Manufacturer", "Price", "Stock"], "")
            for item in range(len(sublist)):
                sublist[item] = inputs[item]  # replace the index with the new ones.

    data_manager.write_table_to_file("store/games.csv", table)
    return table


def get_counts_by_manufacturers(table):
    manufacturer = []
    count = 0  # count from 0
    for i, value in enumerate(table):
        manufacturer.append(value[2])  # if the manufacturer in the list , its gonna take the it to the new list
    ui.print_result(result=dict((i, manufacturer.count(i))
                                for i in manufacturer), label="")  # format to dict and return


def get_average_by_manufacturer(table, manufacturer):

    sum = 0
    amount_of_games = []
    for i, value in enumerate(table):
        if manufacturer[0] in value:
            amount_of_games.append(value[4])
    amount_of_games = list(map(int, amount_of_games))  # convert list to integers
    for num in amount_of_games:
        sum = sum + num
    average = sum / len(amount_of_games)  # get an average

    ui.print_result(result=round(average), label="")
