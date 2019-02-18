""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    options = ["Show table",
               "Add",
               "Remove",
               "Update",
               "What is the id of the item that was sold for the lowest price?",
               "Which items are sold between two given dates? "]
    ui.print_menu("Sales", options, "Back to main menu")

    table = data_manager.get_table_from_file("sales/sales.csv")

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    while True:
        try:
            if option == "1":
                show_table(table)
                break
            elif option == "2":
                return add(table)
            elif option == "3":
                id_ = ui.get_inputs(["Please give me an ID to delete:    "], "")
                remove(table, id_)
                break
            elif option == "4":
                id_ = ui.get_inputs(["Please give me an ID to update:   "], "")
                update(table, id_,)
            elif option == "5":
                get_lowest_price_item_id(table)
                break
            elif option == "6":
                #table, month_from, day_from, year_from, month_to, day_to, year_to = ui.get_inputs(
                 #   ["month_from", "day_from", "year_from", "month_to", "day_to", "year_to"], "")
                get_items_sold_between(table)
                break
            elif option == "0":
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(table, title_list)
    return start_module()


def add(table):
    list_labels = ["Title",
                   "Price",
                   "Month",
                   "Day",
                   "Year"]
    new_id = common.generate_random()
    new_data = ui.get_inputs(list_labels, "")
    new_data.insert(0, new_id)
    table = common.add_line_to_file("sales/sales.csv", new_data)
    return table


def remove(table, id_):
    for i in range(len(table)):
        if table[i][0] == id_:
            del table[i]
            break
        data_manager.write_table_to_file("sales/sales.csv", table)
        return table


def update(table, id_):
    for sublist in table:
        if id_[0] in sublist:
            inputs = ui.get_inputs(["ID", "Title", "Price", "Month", "Day", "Year"], "")
            for item in range(len(sublist)):
                sublist[item] = inputs[item]

    data_manager.write_table_to_file("sales/sales.csv", table)
    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    price = []
    for i, value in enumerate(table):
        price.append(value[2])
    lowest_sold = min(price)
    for i, value in enumerate(table):
        if lowest_sold in value[2]:
            # print(value[0])
            ui.print_result(value[0], label="")


def get_items_sold_between(table):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    date = []
    for i, value in enumerate(table):
        date.append(value[3])
        date.append(value[4])
        date.append(value[5])
    seq = date
    [seq[i:i+3] for i in range(0, len(seq), 3)]
    group_dates=[seq[i:i+3] for i in range(0, len(seq), 3)]
    inputs = ui.get_inputs(["month_from", "day_from", "year_from", "month_to", "day_to", "year_to"], "")
    
    


    # subs = [[]]
    # for i in range(len(date)):
    #        n = i+3
    #
    #        sub = date[i:n]
    #        subs.append(sub)

    # print(subs)
